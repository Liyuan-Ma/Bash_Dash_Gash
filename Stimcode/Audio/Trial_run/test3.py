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
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '0'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np
from numpy.random import randint
import os
import sys
import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
_thisDir = os.path.dirname(os.path.abspath(__file__))
psychopyVersion = '2023.2.1'
expName = 'Trial_mult'
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}

condfile = 'audio_file_paths.csv'

# --- Setup functions for the experiment ---
def showExpInfoDlg(expInfo):
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()
    expInfo.update(poppedKeys)
    return expInfo

def setupData(expInfo, dataDir=None):
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\Lab User\\Documents\\Bash_Dash_Gash\\Stimcode\\Audio\\Trial_run\\Trial_mult_2.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    return thisExp

def setupLogging(filename):
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)
    return logFile

def setupWindow(expInfo=None, win=None):
    if win is None:
        win = visual.Window(
            size=[1536, 864], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        win.color = [-1.0000, -1.0000, -1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win

def setupInputs(expInfo, thisExp, win):
    inputs = {}
    ioConfig = {'Keyboard': dict(use_keymap='psychopy')}
    ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    return {'ioServer': ioServer, 'defaultKeyboard': defaultKeyboard}

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    if thisExp.status != PAUSED:
        return
    for comp in playbackComponents:
        comp.pause()
    win.stashAutoDraw()
    while thisExp.status == PAUSED:
        if inputs is None:
            inputs = {'defaultKeyboard': keyboard.Keyboard(backend='ioHub')}
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        win.flip()
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    for comp in playbackComponents:
        comp.play()
    win.retrieveAutoDraw()
    for timer in timers:
        timer.reset()

def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    thisExp.status = STARTED
    exec = environmenttools.setExecEnvironment(globals())
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    os.chdir(_thisDir)
    filename = thisExp.dataFileName
    frameTolerance = 0.001
    endExpNow = False
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0
    
    # Component initialization and break screen setup
    Instructions = visual.TextStim(win=win, name='Instructions',
        text='Instructions :\n\n“Press 1 for ‘ba’, 2 for ‘da’, and 3 for ‘ga’. \n\nPress space to begin.”\n',
        font='Open Sans', pos=(0, 0), height=0.05, wrapWidth=None, color='white', colorSpace='rgb', opacity=None)
    resp_start = keyboard.Keyboard()
    cross = visual.TextStim(win=win, name='cross', text='+', font='Open Sans', pos=(0, 0), height=0.05, color='white')
    sound_1 = sound.Sound('A', secs=-1, stereo=True, hamming=True, sampleRate=44100)
    breakk = visual.TextStim(win=win, name='breakk',
        text='Take a break. Press space to continue.',
        font='Open Sans', pos=(0, 0), height=0.05, color='white')
    respo_start = keyboard.Keyboard()
    respp = visual.TextStim(win=win, name='respp',
        text='PRESS 1- for BASH, 2 for DASH, and 3 for GASH\n\nReport the sequence: 1    2    3',
        font='Open Sans', pos=(0, 0), height=0.05, color='white')
    key_resp = keyboard.Keyboard()

    if globalClock is None:
        globalClock = core.Clock()
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()
    win.flip()
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # Prepare to start Routine "Instruction"
    continueRoutine = True
    thisExp.addData('Instruction.started', globalClock.getTime())
    resp_start.keys = []
    resp_start.rt = []
    _resp_start_allKeys = []
    InstructionComponents = [Instructions, resp_start]
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    while continueRoutine:
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        
        if Instructions.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            Instructions.frameNStart = frameN
            Instructions.tStart = t
            Instructions.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(Instructions, 'tStartRefresh')
            thisExp.timestampOnFlip(win, 'Instructions.started')
            Instructions.setAutoDraw(True)

        if resp_start.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            resp_start.frameNStart = frameN
            resp_start.tStart = t
            resp_start.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(resp_start, 'tStartRefresh')
            thisExp.timestampOnFlip(win, 'resp_start.started')
            resp_start.status = STARTED
            win.callOnFlip(resp_start.clock.reset)
            win.callOnFlip(resp_start.clearEvents, eventType='keyboard')
        if resp_start.status == STARTED and not waitOnFlip:
            theseKeys = resp_start.getKeys(keyList=['space'], waitRelease=False)
            _resp_start_allKeys.extend(theseKeys)
            if len(_resp_start_allKeys):
                resp_start.keys = _resp_start_allKeys[-1].name
                resp_start.rt = _resp_start_allKeys[-1].rt
                resp_start.duration = _resp_start_allKeys[-1].duration
                continueRoutine = False

        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
            endExperiment(thisExp, win=win, inputs=inputs)
            return
        
        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in InstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        
        if continueRoutine:
            win.flip()
    
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruction.stopped', globalClock.getTime())
    if resp_start.keys in ['', [], None]:
        resp_start.keys = None
    thisExp.addData('resp_start.keys', resp_start.keys)
    if resp_start.keys != None:
        thisExp.addData('resp_start.rt', resp_start.rt)
        thisExp.addData('resp_start.duration', resp_start.duration)
    thisExp.nextEntry()
    routineTimer.reset()
    
    # Set up the trials loop
    trials = data.TrialHandler(nReps=1.0, method='sequential',
        extraInfo=expInfo, trialList=data.importConditions(condfile),
        seed=None, name='trials')
    thisExp.addLoop(trials)
    thisTrial = trials.trialList[0]
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    # Trial loop
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        
        # Check if the current trial is a multiple of 40
        if (trials.thisN + 1) % 40 == 0:
            continueRoutine = True
            routineTimer.reset()
            breakk.setAutoDraw(True)
            respo_start.keys = []
            respo_start.rt = []
            _respo_start_allKeys = []
            while continueRoutine:
                t = routineTimer.getTime()
                theseKeys = respo_start.getKeys(keyList=['space'], waitRelease=False)
                _respo_start_allKeys.extend(theseKeys)
                if len(_respo_start_allKeys):
                    continueRoutine = False
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                    endExperiment(thisExp, win=win, inputs=inputs)
                    return
                win.flip()
            breakk.setAutoDraw(False)

        # Pause experiment if "p" is pressed, resume if "r" is pressed
        if defaultKeyboard.getKeys(keyList=["p"]):
            thisExp.status = PAUSED
            pauseExperiment(thisExp=thisExp, inputs=inputs, win=win, timers=[routineTimer])
        if defaultKeyboard.getKeys(keyList=["r"]):
            thisExp.status = STARTED

        # Prepare to start trial routine
        continueRoutine = True
        thisExp.addData('trial.started', globalClock.getTime())
        sound_1 = sound.Sound(audio, secs=3.750590, hamming=True, stereo=True, sampleRate=44100)
        sound_1.setVolume(1.0)
        sound_1.seek(0)
        trialComponents = [cross, sound_1]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1

        while continueRoutine and routineTimer.getTime() < 5.75059:
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN += 1

            if cross.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                cross.frameNStart = frameN
                cross.tStart = t
                cross.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(cross, 'tStartRefresh')
                thisExp.timestampOnFlip(win, 'cross.started')
                cross.setAutoDraw(True)

            if sound_1.status == NOT_STARTED and t >= 2 - frameTolerance:
                sound_1.frameNStart = frameN
                sound_1.tStart = t
                sound_1.tStartRefresh = tThisFlipGlobal
                thisExp.addData('sound_1.started', t)
                sound_1.status = STARTED
                sound_1.play()

            if sound_1.status == STARTED:
                if tThisFlipGlobal > sound_1.tStartRefresh + 3.750590 - frameTolerance:
                    sound_1.tStop = t
                    sound_1.frameNStop = frameN
                    thisExp.addData('sound_1.stopped', t)
                    sound_1.status = FINISHED
                    sound_1.stop()

            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return

            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            if continueRoutine:
                win.flip()

        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())

        # Prepare for "Responses" routine
        continueRoutine = True
        thisExp.addData('Responses.started', globalClock.getTime())
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        ResponsesComponents = [respp, key_resp]
        for thisComponent in ResponsesComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1

        while continueRoutine and routineTimer.getTime() < 10.00059:
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN += 1

            if respp.status == NOT_STARTED and tThisFlip >= 5.750590 - frameTolerance:
                respp.frameNStart = frameN
                respp.tStart = t
                respp.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(respp, 'tStartRefresh')
                thisExp.timestampOnFlip(win, 'respp.started')
                respp.setAutoDraw(True)

            if key_resp.status == NOT_STARTED and tThisFlip >= 5.750590 - frameTolerance:
                key_resp.frameNStart = frameN
                key_resp.tStart = t
                key_resp.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(key_resp, 'tStartRefresh')
                thisExp.timestampOnFlip(win, 'key_resp.started')
                key_resp.status = STARTED
                win.callOnFlip(key_resp.clock.reset)
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')

            if key_resp.status == STARTED:
                theseKeys = key_resp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys) >= 3:
                    continueRoutine = False

            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return

            if not continueRoutine:
                break
            continueRoutine = False
            for thisComponent in ResponsesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            if continueRoutine:
                win.flip()

        for thisComponent in ResponsesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Responses.stopped', globalClock.getTime())
        if key_resp.keys in ['', [], None]:
            key_resp.keys = None
        trials.addData('key_resp.keys', key_resp.keys)
        if key_resp.keys != None:
            trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.duration', key_resp.duration)
        while len(key_resp.keys) < 3:
            key_resp.keys.append('NA')
        trials.addData('response1', key_resp.keys[0])
        trials.addData('response2', key_resp.keys[1])
        trials.addData('response3', key_resp.keys[2])
        thisExp.nextEntry()

        if thisSession is not None:
            thisSession.sendExperimentData()

    endExperiment(thisExp, win=win, inputs=inputs)

def saveData(thisExp):
    filename = thisExp.dataFileName
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)

def endExperiment(thisExp, inputs=None, win=None):
    if win is not None:
        win.clearAutoDraw()
        win.flip()
    thisExp.status = FINISHED
    if inputs is not None and 'eyetracker' in inputs and inputs['eyetracker'] is not None:
        inputs['eyetracker'].setConnectionState(False)
    logging.flush()

def quit(thisExp, win=None, inputs=None, thisSession=None):
    thisExp.abort()
    if win is not None:
        win.flip()
        win.close()
    if inputs is not None and 'eyetracker' in inputs and inputs['eyetracker'] is not None:
        inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    core.quit()

# Main script execution
if __name__ == '__main__':
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(expInfo=expInfo, thisExp=thisExp, win=win, inputs=inputs)
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
