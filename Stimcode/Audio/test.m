% stimgen_bash_dash_gash.m
% Author: Maanasa Guru Adimurthy and Benjamin Richardson

% Prompt user to enter subject ID
subject_id = input('Enter Subject ID: ', 's');

% Create a folder to save the files
output_folder = sprintf('%s', subject_id);
if ~exist(output_folder, 'dir')
    mkdir(output_folder);
end

% Parameters
fs = 44100; % Sampling rate (Hz)
ITD_us = 600; % Desired ITD in microseconds
ITD_s = ITD_us * 1e-6; % Convert ITD to seconds
delay_samples = round(ITD_s * fs); % Convert ITD to samples

% 400 trials total, with 100 in each condition
num_trials_per_condition = 10; % num trials for each condition, within each block
num_conditions = 4; % total number of conditions (Attend Left/Target Lead, Attend Left/Masker Lead, Attend Right/Target Lead, Attend Left/Masker Lead)
num_blocks = 10; % Number of blocks
words = {'bash','dash','gash'};
[bash, fs] = audioread("bash_normalized.wav");
[dash, fs] = audioread("dash_normalized.wav");
[gash, fs] = audioread("gash_normalized.wav");
audio_files = {bash, dash, gash};
sequence_length = 3;
cue_length = 2 * fs;
cue_audio = [bash; zeros(cue_length - length(bash), 2)];

% Initialize cell arrays to store all sequences for all blocks
all_left_streams = cell(num_blocks, num_trials_per_condition * num_conditions, sequence_length);
all_right_streams = cell(num_blocks, num_trials_per_condition * num_conditions, sequence_length);

for iblock = 1:num_blocks
    % Build attend array for this block
    attend_array = [repmat("left", 1, num_trials_per_condition), repmat("left", 1, num_trials_per_condition), repmat("right", 1, num_trials_per_condition), repmat("right", 1, num_trials_per_condition)];
    % Build lead array for this block
    lead_array = [repmat("target", 1, num_trials_per_condition), repmat("masker", 1, num_trials_per_condition), repmat("target", 1, num_trials_per_condition), repmat("masker", 1, num_trials_per_condition)];
    
    % Randomize condition within block
    condition_array = cat(1, attend_array, lead_array);
    condition_array = condition_array(:, randperm(length(condition_array)));
    
    % Loop through each trial, and build stimulus for this trial
    for itrial = 1:(num_trials_per_condition * num_conditions)
        this_trial_attend = condition_array(1, itrial); % attend condition in this trial
        this_trial_lead = condition_array(2, itrial); % lead condition in this trial
        
        % Initialize cell arrays to store the sequences
        leftStream = cell(1, sequence_length);
        rightStream = cell(1, sequence_length);
        
        % Pick left stream order (with replacement)
        for seq = 1:sequence_length
            % Randomly select a word for the left stream
            leftStream{1, seq} = words{randi(length(words))};
            % Randomly select a word for the right stream
            rightStream{1, seq} = words{randi(length(words))};
        end
        
        % Store sequences
        for seq = 1:sequence_length
            all_left_streams{iblock, itrial, seq} = leftStream{1, seq};
            all_right_streams{iblock, itrial, seq} = rightStream{1, seq};
        end
        
        % Build left stream
        left_audio = [];
        for seq = 1:sequence_length
            word_index = find(strcmp(words, all_left_streams{iblock, itrial, seq}));
            left_audio = [left_audio; audio_files{word_index}];
        end
        
        % Build right stream
        right_audio = [];
        for seq = 1:sequence_length
            word_index = find(strcmp(words, all_right_streams{iblock, itrial, seq}));
            right_audio = [right_audio; audio_files{word_index}];
        end
        
        % Add 250 ms of silence to both streams
        silence_samples = round(0.25 * fs); % 250 ms in samples
        left_audio = [left_audio; zeros(silence_samples, 2)];
        right_audio = [right_audio; zeros(silence_samples, 2)];
        
        % Apply delay to the target or masker in the frequency domain
        L = fft(left_audio);
        R = fft(right_audio);
        f = (0:length(L)-1)' * (fs / length(L));
        
        % ITD application for left and right ear with broadband signal
        if this_trial_lead == "target" % if target is leading
            if this_trial_attend == "right" % target right, so delay left
                L_delayed = L .* exp(-1i * 2 * pi * f * delay_samples / fs);
                left_audio = ifft(L_delayed, 'symmetric');
            else % target left, so delay right
                R_delayed = R .* exp(-1i * 2 * pi * f * delay_samples / fs);
                right_audio = ifft(R_delayed, 'symmetric');
            end
        else
            if this_trial_attend == "left"
                R_delayed = R .* exp(-1i * 2 * pi * f * delay_samples / fs);
                right_audio = ifft(R_delayed, 'symmetric');
            else
                L_delayed = L .* exp(-1i * 2 * pi * f * delay_samples / fs);
                left_audio = ifft(L_delayed, 'symmetric');
            end
        end
        
        % Add the cue to the target stream
        if this_trial_attend == "left"
            left_audio = [cue_audio; left_audio];
            right_audio = [zeros(cue_length, 2); right_audio];
        else
            right_audio = [cue_audio; right_audio];
            left_audio = [zeros(cue_length, 2); left_audio];
        end
        
        % Combine left and right audio into stereo
        stereo_audio = [left_audio, right_audio];
        
        % Save the audio file with correct file extension
        filename = sprintf('%s/block%d_trial%d_attend%s_lead%s.wav', output_folder, iblock, itrial, this_trial_attend, this_trial_lead);
        audiowrite(filename, stereo_audio, fs);
    end
end
