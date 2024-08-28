% audio_rms_bash_dash_gash.m

%% Load sound data
[bash_data,fs] = audioread('bash_praat.wav');
[dash_data,fs] = audioread('dash_praat.wav');
[gash_data,fs] = audioread('gash_praat.wav');

target_length= 22050;
bash_data= bash_data(1:target_length, :);
dash_data= [dash_data; zeros(target_length - length(dash_data), size(dash_data, 2))];
gash_data= [gash_data; zeros(target_length - length(gash_data), size(gash_data, 2))];
%% Calculate RMS

bash_rms_value = rms(bash_data); 
dash_rms_value = rms(dash_data);
gash_rms_value = rms(gash_data); 

%% Normalizing audio RMS value
p0= 20e-6; % Reference sound pressure in Pa
sound_level=70; % Target sound level 70 dB (According to Yuqi's paper)

rmsset= p0* 10^(sound_level/20);

norm_bash = bash_data*rmsset/bash_rms_value;
norm_dash = dash_data*rmsset/dash_rms_value;
norm_gash = gash_data*rmsset/gash_rms_value;
%% Make the normalized audio stereo
norm_bash_stereo = [norm_bash, norm_bash];
norm_dash_stereo = [norm_dash, norm_dash];
norm_gash_stereo = [norm_gash, norm_gash];


[~, name, ext] = fileparts('bash_praat.wav');
outputFileName = fullfile('C:\Users\maana\Documents\GitHub\Bash_Dash_Gash\Stim code\Audio', [name '_normalized' ext]);
audiowrite(outputFileName,norm_bash_stereo, fs);


[~, name, ext] = fileparts('dash_praat.wav');
outputFileName = fullfile('C:\Users\maana\Documents\GitHub\Bash_Dash_Gash\Stim code\Audio', [name '_normalized' ext]);
audiowrite(outputFileName,norm_dash_stereo, fs);


[~, name, ext] = fileparts('gash_praat.wav');
outputFileName = fullfile('C:\Users\maana\Documents\GitHub\Bash_Dash_Gash\Stim code\Audio', [name '_normalized' ext]);
audiowrite(outputFileName,norm_gash_stereo, fs);