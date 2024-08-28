%fixing_onsets.m
%Authors : Maanasa Guru Adimurthy and Benjamin Richardson 

% Load Audio 
[bash,fs]= audioread("bash_praat_normalized.wav");
[dash,fs]= audioread("dash_praat_normalized.wav");
[gash,fs]= audioread("gash_praat_normalized.wav");

% Define the threshold for detecting voice onset
threshold = 0.03;

% Find the onset times
bash_onset = find(abs(bash) > threshold, 1);
dash_onset = find(abs(dash) > threshold, 1);
gash_onset = find(abs(gash) > threshold, 1);

%Find earliest onset time 
earliest_onset = min([bash_onset, dash_onset, gash_onset]);

%align the onsets
dash_diff= dash_onset-earliest_onset;
gash_diff= gash_onset-earliest_onset;
dash_aligned= [dash(dash_diff+1:end,:);dash(1:dash_diff,:)];
gash_aligned= [gash(gash_diff+1:end,:);gash(1:gash_diff,:)];
audiowrite('bash_normalized.wav', bash, fs);
audiowrite('dash_normalized.wav', dash_aligned, fs);
audiowrite('gash_normalized.wav', gash_aligned, fs);