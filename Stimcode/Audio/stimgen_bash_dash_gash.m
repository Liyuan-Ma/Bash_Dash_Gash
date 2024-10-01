% stimgen_bash_dash_gash.m
% Author: Maanasa Guru Adimurthy and Benjamin Richardson

% Prompt user to enter subject ID
subject_id = input('Enter Subject ID: ', 's');

% Create a folder to save the files
output_folder = sprintf('%s', subject_id);
if ~exist(output_folder, 'dir')
    mkdir(output_folder);
end

% 400 trials total, with 100 in each condition
num_trials_per_condition=10; % num trials for each condition, within each block
num_conditions = 4; % total number of conditions (Attend Left/Target Lead, Attend Left/Masker Lead, Attend Right/Target Lead, Attend Left/Masker Lead)
num_blocks=10; % Number of blocks
words= {'bash','dash','gash'} ;
[bash,fs]= audioread("bash_normalized.wav");
[dash,fs]= audioread("dash_normalized.wav");
[gash,fs]= audioread("gash_normalized.wav");
audio_files={bash,dash,gash}
sequence_length= 3;
cue_length=2*fs;
cue_audio = [bash; zeros(cue_length - size(bash,1),size(bash,2))];
% Initialize cell arrays to store all sequences for all blocks
all_left_streams = cell(num_blocks, num_trials_per_condition * num_conditions, sequence_length);
all_right_streams = cell(num_blocks, num_trials_per_condition * num_conditions, sequence_length);
% Initialize a cell array to store file paths
file_paths_counter = 1;
file_paths = cell(num_blocks * num_trials_per_condition * num_conditions, 1); % Create columns for Block, Trial, and File Path
for iblock=1:num_blocks

    % Build attend array for this block
attend_array=[repmat("left",1,num_trials_per_condition),repmat("left",1,num_trials_per_condition),repmat("right",1,num_trials_per_condition),repmat("right",1,num_trials_per_condition) ];
% Build lead array for this block
lead_array=[repmat("target",1,num_trials_per_condition),repmat("masker",1,num_trials_per_condition),repmat("target",1,num_trials_per_condition),repmat("masker",1,num_trials_per_condition)]; 

% Randomize condition within block
condition_array=cat(1,attend_array,lead_array);
condition_array=condition_array(:,randperm(length(condition_array)));


% Loop through each trial, and build stimulus for this trial
for itrial = 1:(num_trials_per_condition*num_conditions)
    this_trial_attend = condition_array(1,itrial); % attend condition in this trial
    this_trial_lead = condition_array(2,itrial); % lead condition in this trial

    
    % Initialize cell arrays to store the sequences
    leftStream = cell(1, sequence_length);
    rightStream = cell(1, sequence_length);
      % Pick left stream order (with replacement)

    % Pick right stream order (with replacement)
     for seq = 1:sequence_length
        % Randomly select a word for the left stream
        leftStream{1,seq} = words{randi(length(words))};
        
        % Randomly select a word for the right stream
        rightStream{1,seq} = words{randi(length(words))};
     end
        for seq = 1:sequence_length
            all_left_streams{iblock, itrial, seq} = leftStream{1, seq};
            all_right_streams{iblock, itrial, seq} = rightStream{1, seq};
        end
          %Build left stream
          % Concatenate audio for left stream
        left_stream_audio = [];
        for seq = 1:sequence_length
            word_index = find(strcmp(words, all_left_streams{iblock, itrial, seq}));
            left_stream_audio = [left_stream_audio; audio_files{word_index}];
        end
        % Build right stream
        % Concatenate audio for right stream
        right_stream_audio = [];
        for seq = 1:sequence_length
            word_index = find(strcmp(words, all_right_streams{iblock, itrial, seq}));
            right_stream_audio = [right_stream_audio; audio_files{word_index}];
        end

        %% Delay lagging stream

        % Add 250 ms of silence to both streams
        delay_samples = round(0.25 * fs); % 250 ms in samples
        left_stream_audio = [left_stream_audio; zeros(delay_samples, size(left_stream_audio, 2))];
        right_stream_audio = [right_stream_audio; zeros(delay_samples, size(right_stream_audio, 2))];
        
        % Apply delay to the target or masker in the frequency domain
        L = fft(left_stream_audio);
        R = fft(right_stream_audio);
        f = (0:length(L)-1)' * (fs / length(L));
        if this_trial_lead == "target" % if target is leading
            if this_trial_attend == "right" % target right, so delay left
                L_delayed = L .* exp(-1i * 2 * pi * f * delay_samples / fs);
                left_stream_audio = ifft(L_delayed, 'symmetric');
            else % target left, so delay right
                R_delayed = R .* exp(-1i * 2 * pi * f * delay_samples / fs);
                right_stream_audio = ifft(R_delayed, 'symmetric');
            end
        else
            if this_trial_attend == "right"
                R_delayed = R .* exp(-1i * 2 * pi * f * delay_samples / fs);
                right_stream_audio = ifft(R_delayed, 'symmetric');
            else
                L_delayed = L .* exp(-1i * 2 * pi * f * delay_samples / fs);
                left_stream_audio = ifft(L_delayed, 'symmetric');
            end
        end
      
        % Add the cue to the target stream
        if this_trial_attend == "left"
            left_stream_audio = [cue_audio; left_stream_audio;zeros(round(600e-6 * fs), 2)];
            right_stream_audio = [zeros(cue_length, 2); right_stream_audio;zeros(round(600e-6 * fs), 2)];
        else
            right_stream_audio = [cue_audio; right_stream_audio;zeros(round(600e-6 * fs), 2)];
            left_stream_audio = [zeros(cue_length, 2); left_stream_audio;zeros(round(600e-6 * fs), 2)];
        end

        % Combine left and right audio into stereo
%         stereo_audio = left_stream_audio + right_stream_audio; %[left_audio(:,1), right_audio(:,2)];
        
         % Desired ITD in microseconds, implement ITD on left and right
         % streams separately
        ITD_s = 600 * 1e-6; % Convert ITD to seconds
        ITD_samples = round(ITD_s * fs); % Convert ITD to samples
        % For the left stream, delay the right ear by ITD_samples samples
        L_ear = fft(left_stream_audio(:,1)); % Left channel
        R_ear = fft(left_stream_audio(:,2)); % Right channel
        f = (0:length(L_ear)-1)' * (fs / length(L_ear));
        R_ear_delayed = R_ear .* exp(-1i * 2 * pi * f * ITD_samples / fs);
        left_stream_audio(:, 1) = ifft(L_ear, 'symmetric');
        left_stream_audio(:, 2) = ifft(R_ear_delayed, 'symmetric');

        % For the right stream, delay the left ear by ITD_samples samples
        L_ear = fft(right_stream_audio(:,1)); % Left channel
        R_ear = fft(right_stream_audio(:,2)); % Right channel
        L_ear_delayed = L_ear .* exp(-1i * 2 * pi * f * ITD_samples / fs);
        right_stream_audio(:, 1) = ifft(L_ear_delayed, 'symmetric');
        right_stream_audio(:, 2) = ifft(R_ear, 'symmetric');
        
         % Combine left and right audio into stereo
        
        trigger_channel= zeros(size(right_stream_audio(:,1)));
       % trigger_channel(1:0.01*fs) = 1;
        trigger_channel(1) = 1;
        stereo_audio = left_stream_audio + right_stream_audio;
        stereo_audio = cat(2,stereo_audio,trigger_channel);
        % Save the audio file with correct file extension
        filename = sprintf('%s/block%d_trial%d_attend%s_lead%s.wav',output_folder, iblock, itrial, this_trial_attend, this_trial_lead);
        audiowrite(filename, stereo_audio, fs);
        [~,filename_only,ext]=fileparts(filename);
        filename_only=strcat(filename_only,ext);
        % Store the block number, trial number, and file path in the cell array
        file_paths{file_paths_counter, 1} = filename_only;
        
        % Increment the file path counter
        file_paths_counter = file_paths_counter + 1;

    end

end
          
index_column=(1:file_paths_counter-1)';

% Convert cell array to a table for easy export to Excel
file_paths_table = table(index_column,file_paths, 'VariableNames', {'Index','audio'});


% Save the table as an Excel file
csv_filename = fullfile(output_folder, 'audio_file_paths.csv');
writetable(file_paths_table, csv_filename);


% Initialize a cell array to store the target word sequences
target_sequences = cell(num_blocks * num_trials_per_condition * num_conditions, sequence_length + 2); % Block, Trial, and 3 Words in the sequence
target_seq_counter = 1;

for iblock=1:num_blocks
    % Build attend array for this block
    attend_array = [repmat("left",1,num_trials_per_condition),repmat("left",1,num_trials_per_condition),repmat("right",1,num_trials_per_condition),repmat("right",1,num_trials_per_condition)];
    % Build lead array for this block
    lead_array = [repmat("target",1,num_trials_per_condition),repmat("masker",1,num_trials_per_condition),repmat("target",1,num_trials_per_condition),repmat("masker",1,num_trials_per_condition)];
    
    % Randomize condition within block
    condition_array = cat(1,attend_array, lead_array);
    condition_array = condition_array(:,randperm(length(condition_array)));

    % Loop through each trial and build stimulus for this trial
    for itrial = 1:(num_trials_per_condition*num_conditions)
        this_trial_attend = condition_array(1, itrial); % Attend condition in this trial
        this_trial_lead = condition_array(2, itrial); % Lead condition in this trial

        % Initialize cell arrays to store the sequences
        leftStream = cell(1, sequence_length);
        rightStream = cell(1, sequence_length);

        % Pick left and right stream order (with replacement)
        for seq = 1:sequence_length
            leftStream{1, seq} = words{randi(length(words))};
            rightStream{1, seq} = words{randi(length(words))};
        end

        % Store the sequences
        for seq = 1:sequence_length
            all_left_streams{iblock, itrial, seq} = leftStream{1, seq};
            all_right_streams{iblock, itrial, seq} = rightStream{1, seq};
        end

        % Save target word sequence based on 'this_trial_attend'
        if this_trial_attend == "left"
            target_sequences{target_seq_counter, 1} = iblock; % Block number
            target_sequences{target_seq_counter, 2} = itrial; % Trial number
            [target_sequences{target_seq_counter, 3},target_sequences{target_seq_counter, 4},target_sequences{target_seq_counter, 5}] = leftStream{:}; % Left stream sequence
        else
            target_sequences{target_seq_counter, 1} = iblock; % Block number
            target_sequences{target_seq_counter, 2} = itrial; % Trial number
            [target_sequences{target_seq_counter, 3},target_sequences{target_seq_counter, 4},target_sequences{target_seq_counter, 5}] = rightStream{:}; % Right stream sequence
        end

        % Increment the target sequence counter
        target_seq_counter = target_seq_counter + 1;

        % The rest of your code for audio processing and file saving goes here...
    end
end

% Convert the target sequences to a table and save it as an Excel file
target_sequences_table = cell2table(target_sequences, 'VariableNames', {'Block', 'Trial', 'Word1', 'Word2', 'Word3'});

% Save the target sequences table as an Excel file
target_excel_filename = fullfile(output_folder, 'target_word_sequences.xlsx');
writetable(target_sequences_table, target_excel_filename, 'WriteVariableNames', true);

