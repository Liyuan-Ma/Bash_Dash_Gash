#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.1),
    on August 27, 2024, at 16:50
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
from psychopy.plugins import activatePlugins
plugins.activatePlugins()
#prefs.hardware['audioLib'] = 'ptb'
#prefs.hardware['audioLatencyMode'] = '0'
#prefs.hardware['audioDevice'] = 'Analog (1+2) (RME Fireface UCX II)'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import sounddevice as sd
import soundfile as sf
import csv
import re
import psychopy.iohub as io
from psychopy.hardware import keyboard
#import serial #Import the serial library

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.1'
expName = 'Trial_mult'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}



def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo
# Display dialog to capture participant ID and other info
expInfo = showExpInfoDlg(expInfo=expInfo)
# Ensure participant ID is not empty and is a valid number
if expInfo['participant'] == '':
    raise ValueError("Participant ID cannot be empty. Please provide a valid numeric ID.")
# Run 'Before Experiment' code from code
subject_folder = os.path.join(_thisDir,expInfo['participant'])
condfile=os.path.join(subject_folder,'audio_file_paths.csv')
# Check if the file exists, to avoid issues if it is not found
if not os.path.exists(condfile):
    raise FileNotFoundError(f"Condition file not found for participant {expInfo['participant']} at {condfile}")

def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\Lab User\\Documents\\Bash_Dash_Gash\\Stimcode\\Audio\\Trial_run\\Trial_mult_2.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
    # return log file
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1920, 1200], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1.0000, -1.0000, -1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }


def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    pausedTimes={}
    # Pause any playback components
    for comp in playbackComponents:
        if hasattr(comp,'getTime'):
            pausedTimes[comp]=comp.getTime()
        if hasattr(comp,'pause'):
            comp.pause()
            
    
        
    #pause message
    pauseMessage= visual.TextStim(win=win,name='Pause',
        text="Experiment Paused\n Press 'c' to continue",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    pauseMessage.setAutoDraw(True)
    win.flip()
    #wait for 'c' to continue
    continueRoutine= True
    while continueRoutine:
        if inputs['defaultKeyboard'].getKeys(keyList=['c']):
            continueRoutine = False
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            core.quit()
        win.flip()
    pauseMessage.setAutoDraw(False)
    win.flip()
    #Resume paused components
    for comp in playbackComponents:
        if hasattr(comp,'seek') and comp in pausedTimes:
            comp.seek(pausedTimes[comp])
        if hasattr(comp,'play'):
            comp.play()
    # Reset timers
    for timer in timers:
        timer.reset()
        
   

def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Instruction" ---
    Instructions = visual.TextStim(win=win, name='Instructions',
        text='Instructions :\n\n“Press 1 for ‘bash’, 2 for ‘dash’, and 3 for ‘gash’. \n\nPress space to begin.”\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    resp_start = keyboard.Keyboard()
    
    # --- Initialize components for Routine "trial" ---
    cross = visual.TextStim(win=win, name='cross',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    #sound_1 = sound.Sound('A', secs=-1, stereo=False, hamming=True,
      #  name='sound_1',sampleRate=44100,)
    #sound_1.setVolume(1.0)
    def play_audio(file_path):
        audio_data,sample_rate=sf.read(file_path)
        sd.default.device='ASIO Fireface USB'
        
        
        sd.play(audio_data,samplerate=sample_rate,mapping=[1,2,3])
        sd.wait()
    def extract_block_number(audio_filename):
        match=re.search(r'block(\d+)',audio_filename)
        if match:
            return(int(match.group(1)))
        else:
            return None
        
        
    
    
    
    # --- Initialize components for Routine "break" ---
    breakk = visual.TextStim(win=win, name='breakk',
        text='Instructions :\n\n“Take a break \n\nPress space to continue.”\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    respo_start = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Responses" ---
    respp = visual.TextStim(win=win, name='respp',
        text='Report the sequence :\n\n    1                    2                   3\nBASH            DASH          GASH',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "Instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruction.started', globalClock.getTime())
    resp_start.keys = []
    resp_start.rt = []
    _resp_start_allKeys = []
    # keep track of which components have finished
    InstructionComponents = [Instructions, resp_start]
    for thisComponent in InstructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
   
    
    # --- Run Routine "Instruction" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
         # check for pause key
        if inputs['defaultKeyboard'].getKeys(keyList=['p']):
            pauseExperiment(thisExp, inputs=inputs, win=win, playbackComponents=[sound_1], timers=[routineTimer])
        theseKeys = resp_start.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            continueRoutine=False
        # Check if escape is pressed to quit
        if defaultKeyboard.getKeys(keyList=["escape"]):
            endExperiment(thisExp, inputs=inputs, win=win)
            core.quit()
        if continueRoutine:
            win.flip()
            
        # *Instructions* updates
        
        # if Instructions is starting this frame...
        if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions.frameNStart = frameN  # exact frame index
            Instructions.tStart = t  # local t and not account for scr refresh
            Instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions.started')
            # update status
            Instructions.status = STARTED 
            Instructions.setAutoDraw(True)
        
        # if Instructions is active this frame...
        if Instructions.status == STARTED:
            # update params
            pass
        
        # if Instructions is stopping this frame...
        if Instructions.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Instructions.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                Instructions.tStop = t  # not accounting for scr refresh
                Instructions.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Instructions.stopped')
                # update status
                Instructions.status = FINISHED
                Instructions.setAutoDraw(False)
        
        # *resp_start* updates
        waitOnFlip = False
        
        # if resp_start is starting this frame...
        if resp_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_start.frameNStart = frameN  # exact frame index
            resp_start.tStart = t  # local t and not account for scr refresh
            resp_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_start, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp_start.started')
            # update status
            resp_start.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_start.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_start.status == STARTED and not waitOnFlip:
            theseKeys = resp_start.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _resp_start_allKeys.extend(theseKeys)
            if len(_resp_start_allKeys):
                resp_start.keys = _resp_start_allKeys[-1].name  # just the last key pressed
                resp_start.rt = _resp_start_allKeys[-1].rt
                resp_start.duration = _resp_start_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction" ---
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruction.stopped', globalClock.getTime())
    # check responses
    if resp_start.keys in ['', [], None]:  # No response was made
        resp_start.keys = None
    thisExp.addData('resp_start.keys',resp_start.keys)
    if resp_start.keys != None:  # we had a response
        thisExp.addData('resp_start.rt', resp_start.rt)
        thisExp.addData('resp_start.duration', resp_start.duration)
    thisExp.nextEntry()
    # the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condfile),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    #current_block=None
    
    previous_block=None
    for thisTrial in trials:
        #check if 'p' is pressed
        
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        #audio_file=thisTrial['audio']
        current_block=extract_block_number(thisTrial['audio'])
        
            #check if the current trial number is a multiple of 40
        if current_block is not None and current_block != previous_block:
            if previous_block is not None:
                
                
                
        #if trials.thisN >= 0 and (trials.thisN+1) % 40 == 0:
                continueRoutine = True
                routineTimer.reset()
                
                #Start break routine
                breakk.setAutoDraw(True)
                respo_start.keys=[]
                respo_start.rt=[]
                _respo_start_allKeys=[]
                while continueRoutine: 
                    t=routineTimer.getTime()
                    theseKeys=respo_start.getKeys(keyList=['space'],waitRelease=False)
                    _respo_start_allKeys.extend(theseKeys)
                    if len(_respo_start_allKeys):
                        continueRoutine=False
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status=FINISHED
                        endExperiment(thisExp,inputs=inputs,win=win)
                        return
                    win.flip()
                breakk.setAutoDraw(False)
                #reset routineTimer
                routineTimer.reset()
            previous_block=current_block 
                
        
            
        if inputs['defaultKeyboard'].getKeys(keyList=['p']):
            pauseExperiment(thisExp,inputs=inputs,win=win, playbackComponents=[sound_1], timers=[routineTimer])
        win.flip()
        # pause experiment here if requested
        #if thisExp.status == PAUSED:
         #   pauseExperiment(
          #      thisExp=thisExp, 
           #     inputs=inputs, 
            #    win=win, 
             #   timers=[routineTimer], 
              #  playbackComponents=[]
        #)
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        #if thisTrial != None:
           # for paramName in thisTrial:
             #   globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        audio_file_path = os.path.join(subject_folder,thisTrial['audio'])
        
        #sound_1=sound.Sound(audio_file_path, secs=3.750590, hamming=True, stereo=True, sampleRate=44100)
        #sound_1.setVolume(1.0, log=False)
        #sound_1.seek(0)
        # keep track of which components have finished
        trialComponents = [cross] #, sound_1
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.75059:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            #if inputs['defaultKeyboard'].getKeys(key ts,win=win, playbackComponents=[sound_1], timers=[routineTimer])
                
            # *cross* updates
            
            # if cross is starting this frame...
            if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.started')
                # update status
                cross.status = STARTED
                cross.setAutoDraw(True)
            
            # if cross is active this frame...
            if cross.status == STARTED:
                # update params
                pass
            
            # if cross is stopping this frame...
            if cross.status == STARTED:
                # win.callOnFlip(port.write, str.encode('0'))
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross.tStartRefresh + 5.750590-frameTolerance:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross.stopped')
                    # update status
                    cross.status = FINISHED
                    cross.setAutoDraw(False)
                    
            # if sound_1 is starting this frame...
            if t >= 2-frameTolerance:  #if sound_1.status == NOT_STARTED and t >= 2-frameTolerance:
                #trigger_value = 1
                #win.callOnFlip(port.write, trigger_value)
                # keep track of start time/frame for later
                #sound_1.frameNStart = frameN  # exact frame index
                #sound_1.tStart = t  # local t and not account for scr refresh
                #sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('audio.started', t)
                # update status
                #sound_1.status = STARTED
                 # write a trigger to the port
                #sound_1.play()  # start the sound (it finishes automatically)
                play_audio(audio_file_path)
            
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status =FINISHED
                endExperiment(thisExp, inputs=inputs, win=win)
                core.quit()
            if continueRoutine:
                win.flip()
                
            
            # if sound_1 is stopping this frame... 
            #if sound_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                #if sound_1.tStartRefresh is not None and tThisFlipGlobal > sound_1.tStartRefresh + 3.750590-frameTolerance: 
                    # keep track of stop time/frame for later
                   # sound_1.tStop = t  # not accounting for scr refresh
                   # sound_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    #thisExp.addData('sound_1.stopped', t)
                    # update status
                    #sound_1.status = FINISHED
                   # sound_1.stop()
            # update sound_1 status according to whether it's playing
           # if sound_1.isPlaying:
            #    sound_1.status = STARTED
           # elif sound_1.isFinished:
             #   sound_1.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            pass
        
        # --- Prepare to start Routine "Responses" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Responses.started', globalClock.getTime())
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # Run 'Begin Routine' code from Resp_code
        key_resp.keys = []  # Initialize an empty list to store key responses
        
        # keep track of which components have finished
        ResponsesComponents = [respp, key_resp]
        for thisComponent in ResponsesComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Responses" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.000589999999999:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if inputs['defaultKeyboard'].getKeys(keyList=['p']):
                pauseExperiment(thisExp,inputs=inputs,win=win, playbackComponents=[sound_1], timers=[routineTimer])
            # *respp* updates
            
            # if respp is starting this frame...
            if respp.status == NOT_STARTED and tThisFlip >= 5.750590-frameTolerance:
                # keep track of start time/frame for later
                respp.frameNStart = frameN  # exact frame index
                respp.tStart = t  # local t and not account for scr refresh
                respp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respp.started')
                # update status
                respp.status = STARTED
                respp.setAutoDraw(True)
            
            # if respp is active this frame...
            if respp.status == STARTED:
                # update params
                pass
            
            # if respp is stopping this frame...
            if respp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > respp.tStartRefresh + 4.25-frameTolerance:
                    # keep track of stop time/frame for later
                    respp.tStop = t  # not accounting for scr refresh
                    respp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'respp.stopped')
                    # update status
                    respp.status = FINISHED
                    respp.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 5.750590-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp is stopping this frame...
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 4.25-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    # update status
                    key_resp.status = FINISHED
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['1','2','3'], ignoreKeys=["escape"], waitRelease=True)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                    key_resp.rt = [key.rt for key in _key_resp_allKeys]
                    key_resp.duration = [key.duration for key in _key_resp_allKeys]
            # Run 'Each Frame' code from Resp_code
            # Get the keys pressed in this frame
            theseKeys = key_resp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            if key_resp.keys is None:
                key_resp.keys=[]
            # Store each key pressed in the list, but only if less than 3 keys have been pressed
            for key in theseKeys:
                if len(key_resp.keys) < 3:
                    key_resp.keys.append(key.name)
            
            # End the routine if three keys have been recorded
            if len(key_resp.keys) == 3:
                continueRoutine = False
            
            
            # check for quit (typically the Esc key)
            if inputs['defaultKeyboard'].getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win, playbackComponents=[sound_1], timers=[routineTimer])
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ResponsesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Responses" ---
        for thisComponent in ResponsesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Responses.stopped', globalClock.getTime())
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.duration', key_resp.duration)
        # Run 'End Routine' code from Resp_code
        # Ensure we have exactly three responses recorded; if not, fill with 'NA'
        if key_resp.keys is None:
            key_resp.keys=[]
        while len(key_resp.keys) < 3:
            key_resp.keys.append('NA')
        
        # Store the responses in the data file
        trials.addData('response1', key_resp.keys[0])
        trials.addData('response2', key_resp.keys[1])
        trials.addData('response3', key_resp.keys[2])
        
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000590)
        
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials'
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            eyetracker.setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    #port = serial.Serial('COM4', baudrate=115200) #Change 'COM3' here to your serial port address
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
   # port.close()
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
