#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Tue Jan 21 10:29:27 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Project 1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/laurenvomberg/Documents/U of T classes/Fall 2019/Coding/Project 1/Project 1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='In this study you will hear a series of short musical melodies. Your job is to identify how many melodies you hear at once, and how easy it is to distinguish between the separate melodies. You will indicate your response by clicking on the statement that best fits what you heard, followed by the return (enter) key to proceed to the next melody. If you have any questions, please ask the experimenter. To continue, please click the space-bar.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

#Please refer to the outline for a description of how this routine was compiled
#secs=400 to control for speed
#volume consistently 1 but can be manipulated if needed
# Initialize components for Routine "trial_IOI_L_400"
trial_IOI_L_400Clock = core.Clock()
sound_1_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_1_L')
sound_1_L.setVolume(1)
sound_2_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_2_L')
sound_2_L.setVolume(1)
sound_3_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_3_L')
sound_3_L.setVolume(1)
sound_4_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_4_L')
sound_4_L.setVolume(1)
sound_5_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_5_L')
sound_5_L.setVolume(1)
sound_6_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_6_L')
sound_6_L.setVolume(1)
sound_7_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_7_L')
sound_7_L.setVolume(1)
sound_8_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_8_L')
sound_8_L.setVolume(1)
sound_9_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_9_L')
sound_9_L.setVolume(1)
sound_10_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_10_L')
sound_10_L.setVolume(1)
sound_11_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_11_L')
sound_11_L.setVolume(1)
sound_12_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_12_L')
sound_12_L.setVolume(1)
sound_13_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_13_L')
sound_13_L.setVolume(1)
sound_14_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_14_L')
sound_14_L.setVolume(1)
sound_15_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_15_L')
sound_15_L.setVolume(1)
sound_16_L = sound.Sound('A', secs=0.4, stereo=True, hamming=True,
    name='sound_16_L')
sound_16_L.setVolume(1)
HowManyMelodies_IOI_L = visual.TextStim(win=win, name='HowManyMelodies_IOI_L',
    text='How many melodies do you hear? Please indicate your response on the scale below then hit the enter/return key to proceed to the next melody.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=2.0, pos=[0.0, -0.4], choices=['easy to hear \n one melody', 'moderately able to \n hear one melody', 'hard to hear \n one melody', 'hard to hear \n two melodies', 'moderately able to \n hear two melodies', 'easy to hear \n two melodies'], tickHeight=-1, textSize=.3, showAccept=False)

# Initialize components for Routine "trial_IOI_M_250"
#Please refer to the outline for a description of how this routine was compiled
#secs=250 to control for speed
trial_IOI_M_250Clock = core.Clock()
sound_1_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_1_M')
sound_1_M.setVolume(1)
sound_2_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_2_M')
sound_2_M.setVolume(1)
sound_3_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_3_M')
sound_3_M.setVolume(1)
sound_4_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_4_M')
sound_4_M.setVolume(1)
sound_5_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_5_M')
sound_5_M.setVolume(1)
sound_6_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_6_M')
sound_6_M.setVolume(1)
sound_7_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_7_M')
sound_7_M.setVolume(1)
sound_8_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_8_M')
sound_8_M.setVolume(1)
sound_9_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_9_M')
sound_9_M.setVolume(1)
sound_10_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_10_M')
sound_10_M.setVolume(1)
sound_11_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_11_M')
sound_11_M.setVolume(1)
sound_12_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_12_M')
sound_12_M.setVolume(1)
sound_13_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_13_M')
sound_13_M.setVolume(1)
sound_14_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_14_M')
sound_14_M.setVolume(1)
sound_15_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_15_M')
sound_15_M.setVolume(1)
sound_16_M = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_16_M')
sound_16_M.setVolume(1)
HowManyMelodies_IOI_M = visual.TextStim(win=win, name='HowManyMelodies_IOI_M',
    text='How many melodies do you hear? Please indicate your response on the scale below then hit the enter/return key to proceed to the next melody.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
rating_2 = visual.RatingScale(win=win, name='rating_2', marker='triangle', size=2.0, pos=[0.0, -0.4], choices=['easy to hear \n one melody', 'moderately able to \n hear one melody', 'hard to hear \n one melody', 'hard to hear \n two melodies', 'moderately able to \n hear two melodies', 'easy to hear \n two melodies'], tickHeight=-1, textSize=.3, showAccept=False)

# Initialize components for Routine "trial_IOI_S_125"
#Please refer to the outline for a description of how this routine was compiled
#secs=125 to control for speed
trial_IOI_S_125Clock = core.Clock()
sound_1_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_1_S')
sound_1_S.setVolume(1)
sound_2_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_2_S')
sound_2_S.setVolume(1)
sound_3_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_3_S')
sound_3_S.setVolume(1)
sound_4_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_4_S')
sound_4_S.setVolume(1)
sound_5_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_5_S')
sound_5_S.setVolume(1)
sound_6_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_6_S')
sound_6_S.setVolume(1)
sound_7_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_7_S')
sound_7_S.setVolume(1)
sound_8_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_8_S')
sound_8_S.setVolume(1)
sound_9_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_9_S')
sound_9_S.setVolume(1)
sound_10_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_10_S')
sound_10_S.setVolume(1)
sound_11_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_11_S')
sound_11_S.setVolume(1)
sound_12_S = sound.Sound('A', secs=0.125, stereo=True, hamming=False,
    name='sound_12_S')
sound_12_S.setVolume(1)
sound_13_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_13_S')
sound_13_S.setVolume(1)
sound_14_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_14_S')
sound_14_S.setVolume(1)
sound_15_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_15_S')
sound_15_S.setVolume(1)
sound_16_S = sound.Sound('A', secs=0.125, stereo=True, hamming=True,
    name='sound_16_S')
sound_16_S.setVolume(1)
HowManyMelodies_IOI_S = visual.TextStim(win=win, name='HowManyMelodies_IOI_S',
    text='How many melodies do you hear? Please indicate your response on the scale below then hit the enter/return key to proceed to the next melody.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
rating_3 = visual.RatingScale(win=win, name='rating_3', marker='triangle', size=2.0, pos=[0.0, -0.4], choices=['easy to hear \n one melody', 'moderately able to \n hear one melody', 'hard to hear \n one melody', 'hard to hear \n two melodies', 'moderately able to \n hear two melodies', 'easy to hear \n two melodies'], tickHeight=-1, textSize=.3, showAccept=False)

# Initialize components for Routine "Finished"
FinishedClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Thank you for participating in this study!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
InstructionsComponents = [text, key_resp]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
IOI_L = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('IOI_L.xlsx'),
    seed=None, name='IOI_L')
thisExp.addLoop(IOI_L)  # add the loop to the experiment
thisIOI_L = IOI_L.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIOI_L.rgb)
if thisIOI_L != None:
    for paramName in thisIOI_L:
        exec('{} = thisIOI_L[paramName]'.format(paramName))

for thisIOI_L in IOI_L:
    currentLoop = IOI_L
    # abbreviate parameter names if possible (e.g. rgb = thisIOI_L.rgb)
    if thisIOI_L != None:
        for paramName in thisIOI_L:
            exec('{} = thisIOI_L[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_IOI_L_400"-------
    # update component parameters for each repeat
    sound_1_L.setSound(S1, secs=0.4, hamming=True)
    sound_1_L.setVolume(1, log=False)
    sound_2_L.setSound(S2, secs=0.4, hamming=True)
    sound_2_L.setVolume(1, log=False)
    sound_3_L.setSound(S3, secs=0.4, hamming=True)
    sound_3_L.setVolume(1, log=False)
    sound_4_L.setSound(S4, secs=0.4, hamming=True)
    sound_4_L.setVolume(1, log=False)
    sound_5_L.setSound(S5, secs=0.4, hamming=True)
    sound_5_L.setVolume(1, log=False)
    sound_6_L.setSound(S6, secs=0.4, hamming=True)
    sound_6_L.setVolume(1, log=False)
    sound_7_L.setSound(S7, secs=0.4, hamming=True)
    sound_7_L.setVolume(1, log=False)
    sound_8_L.setSound(S8, secs=0.4, hamming=True)
    sound_8_L.setVolume(1, log=False)
    sound_9_L.setSound(S9, secs=0.4, hamming=True)
    sound_9_L.setVolume(1, log=False)
    sound_10_L.setSound(S10, secs=0.4, hamming=True)
    sound_10_L.setVolume(1, log=False)
    sound_11_L.setSound(S11, secs=0.4, hamming=True)
    sound_11_L.setVolume(1, log=False)
    sound_12_L.setSound(S12, secs=0.4, hamming=True)
    sound_12_L.setVolume(1, log=False)
    sound_13_L.setSound(S13, secs=0.4, hamming=True)
    sound_13_L.setVolume(1, log=False)
    sound_14_L.setSound(S14, secs=0.4, hamming=True)
    sound_14_L.setVolume(1, log=False)
    sound_15_L.setSound(S16, secs=0.4, hamming=True)
    sound_15_L.setVolume(1, log=False)
    sound_16_L.setSound(S16, secs=0.4, hamming=True)
    sound_16_L.setVolume(1, log=False)
    rating.reset()
    # keep track of which components have finished
    trial_IOI_L_400Components = [sound_1_L, sound_2_L, sound_3_L, sound_4_L, sound_5_L, sound_6_L, sound_7_L, sound_8_L, sound_9_L, sound_10_L, sound_11_L, sound_12_L, sound_13_L, sound_14_L, sound_15_L, sound_16_L, HowManyMelodies_IOI_L, rating]
    for thisComponent in trial_IOI_L_400Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_IOI_L_400Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_IOI_L_400"-------
    while continueRoutine:
        # get current time
        t = trial_IOI_L_400Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_IOI_L_400Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1_L
        if sound_1_L.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            sound_1_L.frameNStart = frameN  # exact frame index
            sound_1_L.tStart = t  # local t and not account for scr refresh
            sound_1_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1_L.play(when=win)  # sync with win flip
        if sound_1_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_1_L.tStop = t  # not accounting for scr refresh
                sound_1_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1_L, 'tStopRefresh')  # time at next scr refresh
                sound_1_L.stop()
        # start/stop sound_2_L
        if sound_2_L.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
            # keep track of start time/frame for later
            sound_2_L.frameNStart = frameN  # exact frame index
            sound_2_L.tStart = t  # local t and not account for scr refresh
            sound_2_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2_L.play(when=win)  # sync with win flip
        if sound_2_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_2_L.tStop = t  # not accounting for scr refresh
                sound_2_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2_L, 'tStopRefresh')  # time at next scr refresh
                sound_2_L.stop()
        # start/stop sound_3_L
        if sound_3_L.status == NOT_STARTED and tThisFlip >= 1.3-frameTolerance:
            # keep track of start time/frame for later
            sound_3_L.frameNStart = frameN  # exact frame index
            sound_3_L.tStart = t  # local t and not account for scr refresh
            sound_3_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_3_L.play(when=win)  # sync with win flip
        if sound_3_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_3_L.tStop = t  # not accounting for scr refresh
                sound_3_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_3_L, 'tStopRefresh')  # time at next scr refresh
                sound_3_L.stop()
        # start/stop sound_4_L
        if sound_4_L.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
            # keep track of start time/frame for later
            sound_4_L.frameNStart = frameN  # exact frame index
            sound_4_L.tStart = t  # local t and not account for scr refresh
            sound_4_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_4_L.play(when=win)  # sync with win flip
        if sound_4_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_4_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_4_L.tStop = t  # not accounting for scr refresh
                sound_4_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_4_L, 'tStopRefresh')  # time at next scr refresh
                sound_4_L.stop()
        # start/stop sound_5_L
        if sound_5_L.status == NOT_STARTED and tThisFlip >= 2.1-frameTolerance:
            # keep track of start time/frame for later
            sound_5_L.frameNStart = frameN  # exact frame index
            sound_5_L.tStart = t  # local t and not account for scr refresh
            sound_5_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_5_L.play(when=win)  # sync with win flip
        if sound_5_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_5_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_5_L.tStop = t  # not accounting for scr refresh
                sound_5_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_5_L, 'tStopRefresh')  # time at next scr refresh
                sound_5_L.stop()
        # start/stop sound_6_L
        if sound_6_L.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            sound_6_L.frameNStart = frameN  # exact frame index
            sound_6_L.tStart = t  # local t and not account for scr refresh
            sound_6_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_6_L.play(when=win)  # sync with win flip
        if sound_6_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_6_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_6_L.tStop = t  # not accounting for scr refresh
                sound_6_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_6_L, 'tStopRefresh')  # time at next scr refresh
                sound_6_L.stop()
        # start/stop sound_7_L
        if sound_7_L.status == NOT_STARTED and tThisFlip >= 2.9-frameTolerance:
            # keep track of start time/frame for later
            sound_7_L.frameNStart = frameN  # exact frame index
            sound_7_L.tStart = t  # local t and not account for scr refresh
            sound_7_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_7_L.play(when=win)  # sync with win flip
        if sound_7_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_7_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_7_L.tStop = t  # not accounting for scr refresh
                sound_7_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_7_L, 'tStopRefresh')  # time at next scr refresh
                sound_7_L.stop()
        # start/stop sound_8_L
        if sound_8_L.status == NOT_STARTED and tThisFlip >= 3.3-frameTolerance:
            # keep track of start time/frame for later
            sound_8_L.frameNStart = frameN  # exact frame index
            sound_8_L.tStart = t  # local t and not account for scr refresh
            sound_8_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_8_L.play(when=win)  # sync with win flip
        if sound_8_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_8_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_8_L.tStop = t  # not accounting for scr refresh
                sound_8_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_8_L, 'tStopRefresh')  # time at next scr refresh
                sound_8_L.stop()
        # start/stop sound_9_L
        if sound_9_L.status == NOT_STARTED and tThisFlip >= 3.7-frameTolerance:
            # keep track of start time/frame for later
            sound_9_L.frameNStart = frameN  # exact frame index
            sound_9_L.tStart = t  # local t and not account for scr refresh
            sound_9_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_9_L.play(when=win)  # sync with win flip
        if sound_9_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_9_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_9_L.tStop = t  # not accounting for scr refresh
                sound_9_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_9_L, 'tStopRefresh')  # time at next scr refresh
                sound_9_L.stop()
        # start/stop sound_10_L
        if sound_10_L.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
            # keep track of start time/frame for later
            sound_10_L.frameNStart = frameN  # exact frame index
            sound_10_L.tStart = t  # local t and not account for scr refresh
            sound_10_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_10_L.play(when=win)  # sync with win flip
        if sound_10_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_10_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_10_L.tStop = t  # not accounting for scr refresh
                sound_10_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_10_L, 'tStopRefresh')  # time at next scr refresh
                sound_10_L.stop()
        # start/stop sound_11_L
        if sound_11_L.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
            # keep track of start time/frame for later
            sound_11_L.frameNStart = frameN  # exact frame index
            sound_11_L.tStart = t  # local t and not account for scr refresh
            sound_11_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_11_L.play(when=win)  # sync with win flip
        if sound_11_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_11_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_11_L.tStop = t  # not accounting for scr refresh
                sound_11_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_11_L, 'tStopRefresh')  # time at next scr refresh
                sound_11_L.stop()
        # start/stop sound_12_L
        if sound_12_L.status == NOT_STARTED and tThisFlip >= 4.9-frameTolerance:
            # keep track of start time/frame for later
            sound_12_L.frameNStart = frameN  # exact frame index
            sound_12_L.tStart = t  # local t and not account for scr refresh
            sound_12_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_12_L.play(when=win)  # sync with win flip
        if sound_12_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_12_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_12_L.tStop = t  # not accounting for scr refresh
                sound_12_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_12_L, 'tStopRefresh')  # time at next scr refresh
                sound_12_L.stop()
        # start/stop sound_13_L
        if sound_13_L.status == NOT_STARTED and tThisFlip >= 5.3-frameTolerance:
            # keep track of start time/frame for later
            sound_13_L.frameNStart = frameN  # exact frame index
            sound_13_L.tStart = t  # local t and not account for scr refresh
            sound_13_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_13_L.play(when=win)  # sync with win flip
        if sound_13_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_13_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_13_L.tStop = t  # not accounting for scr refresh
                sound_13_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_13_L, 'tStopRefresh')  # time at next scr refresh
                sound_13_L.stop()
        # start/stop sound_14_L
        if sound_14_L.status == NOT_STARTED and tThisFlip >= 5.7-frameTolerance:
            # keep track of start time/frame for later
            sound_14_L.frameNStart = frameN  # exact frame index
            sound_14_L.tStart = t  # local t and not account for scr refresh
            sound_14_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_14_L.play(when=win)  # sync with win flip
        if sound_14_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_14_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_14_L.tStop = t  # not accounting for scr refresh
                sound_14_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_14_L, 'tStopRefresh')  # time at next scr refresh
                sound_14_L.stop()
        # start/stop sound_15_L
        if sound_15_L.status == NOT_STARTED and tThisFlip >= 6.1-frameTolerance:
            # keep track of start time/frame for later
            sound_15_L.frameNStart = frameN  # exact frame index
            sound_15_L.tStart = t  # local t and not account for scr refresh
            sound_15_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_15_L.play(when=win)  # sync with win flip
        if sound_15_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_15_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_15_L.tStop = t  # not accounting for scr refresh
                sound_15_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_15_L, 'tStopRefresh')  # time at next scr refresh
                sound_15_L.stop()
        # start/stop sound_16_L
        if sound_16_L.status == NOT_STARTED and tThisFlip >= 6.5-frameTolerance:
            # keep track of start time/frame for later
            sound_16_L.frameNStart = frameN  # exact frame index
            sound_16_L.tStart = t  # local t and not account for scr refresh
            sound_16_L.tStartRefresh = tThisFlipGlobal  # on global time
            sound_16_L.play(when=win)  # sync with win flip
        if sound_16_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_16_L.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                sound_16_L.tStop = t  # not accounting for scr refresh
                sound_16_L.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_16_L, 'tStopRefresh')  # time at next scr refresh
                sound_16_L.stop()
        
        # *HowManyMelodies_IOI_L* updates
        if HowManyMelodies_IOI_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HowManyMelodies_IOI_L.frameNStart = frameN  # exact frame index
            HowManyMelodies_IOI_L.tStart = t  # local t and not account for scr refresh
            HowManyMelodies_IOI_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HowManyMelodies_IOI_L, 'tStartRefresh')  # time at next scr refresh
            HowManyMelodies_IOI_L.setAutoDraw(True)
        # *rating* updates
        if rating.status == NOT_STARTED and t >= 6.9-frameTolerance:
            # keep track of start time/frame for later
            rating.frameNStart = frameN  # exact frame index
            rating.tStart = t  # local t and not account for scr refresh
            rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_IOI_L_400Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_IOI_L_400"-------
    for thisComponent in trial_IOI_L_400Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_1_L.started', sound_1_L.tStartRefresh)
    IOI_L.addData('sound_1_L.stopped', sound_1_L.tStopRefresh)
    sound_2_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_2_L.started', sound_2_L.tStartRefresh)
    IOI_L.addData('sound_2_L.stopped', sound_2_L.tStopRefresh)
    sound_3_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_3_L.started', sound_3_L.tStartRefresh)
    IOI_L.addData('sound_3_L.stopped', sound_3_L.tStopRefresh)
    sound_4_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_4_L.started', sound_4_L.tStartRefresh)
    IOI_L.addData('sound_4_L.stopped', sound_4_L.tStopRefresh)
    sound_5_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_5_L.started', sound_5_L.tStartRefresh)
    IOI_L.addData('sound_5_L.stopped', sound_5_L.tStopRefresh)
    sound_6_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_6_L.started', sound_6_L.tStartRefresh)
    IOI_L.addData('sound_6_L.stopped', sound_6_L.tStopRefresh)
    sound_7_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_7_L.started', sound_7_L.tStartRefresh)
    IOI_L.addData('sound_7_L.stopped', sound_7_L.tStopRefresh)
    sound_8_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_8_L.started', sound_8_L.tStartRefresh)
    IOI_L.addData('sound_8_L.stopped', sound_8_L.tStopRefresh)
    sound_9_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_9_L.started', sound_9_L.tStartRefresh)
    IOI_L.addData('sound_9_L.stopped', sound_9_L.tStopRefresh)
    sound_10_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_10_L.started', sound_10_L.tStartRefresh)
    IOI_L.addData('sound_10_L.stopped', sound_10_L.tStopRefresh)
    sound_11_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_11_L.started', sound_11_L.tStartRefresh)
    IOI_L.addData('sound_11_L.stopped', sound_11_L.tStopRefresh)
    sound_12_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_12_L.started', sound_12_L.tStartRefresh)
    IOI_L.addData('sound_12_L.stopped', sound_12_L.tStopRefresh)
    sound_13_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_13_L.started', sound_13_L.tStartRefresh)
    IOI_L.addData('sound_13_L.stopped', sound_13_L.tStopRefresh)
    sound_14_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_14_L.started', sound_14_L.tStartRefresh)
    IOI_L.addData('sound_14_L.stopped', sound_14_L.tStopRefresh)
    sound_15_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_15_L.started', sound_15_L.tStartRefresh)
    IOI_L.addData('sound_15_L.stopped', sound_15_L.tStopRefresh)
    sound_16_L.stop()  # ensure sound has stopped at end of routine
    IOI_L.addData('sound_16_L.started', sound_16_L.tStartRefresh)
    IOI_L.addData('sound_16_L.stopped', sound_16_L.tStopRefresh)
    IOI_L.addData('HowManyMelodies_IOI_L.started', HowManyMelodies_IOI_L.tStartRefresh)
    IOI_L.addData('HowManyMelodies_IOI_L.stopped', HowManyMelodies_IOI_L.tStopRefresh)
    # store data for IOI_L (TrialHandler)
    IOI_L.addData('rating.response', rating.getRating())
    IOI_L.addData('rating.rt', rating.getRT())
    IOI_L.addData('rating.started', rating.tStart)
    IOI_L.addData('rating.stopped', rating.tStop)
    # the Routine "trial_IOI_L_400" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'IOI_L'


# set up handler to look after randomisation of conditions etc
IOI_M = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('IOI_M.xlsx'),
    seed=None, name='IOI_M')
thisExp.addLoop(IOI_M)  # add the loop to the experiment
thisIOI_M = IOI_M.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIOI_M.rgb)
if thisIOI_M != None:
    for paramName in thisIOI_M:
        exec('{} = thisIOI_M[paramName]'.format(paramName))

for thisIOI_M in IOI_M:
    currentLoop = IOI_M
    # abbreviate parameter names if possible (e.g. rgb = thisIOI_M.rgb)
    if thisIOI_M != None:
        for paramName in thisIOI_M:
            exec('{} = thisIOI_M[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_IOI_M_250"-------
    # update component parameters for each repeat
    sound_1_M.setSound(S1, secs=0.25, hamming=True)
    sound_1_M.setVolume(1, log=False)
    sound_2_M.setSound(S2, secs=0.25, hamming=True)
    sound_2_M.setVolume(1, log=False)
    sound_3_M.setSound(S3, secs=0.25, hamming=True)
    sound_3_M.setVolume(1, log=False)
    sound_4_M.setSound(S4, secs=0.25, hamming=True)
    sound_4_M.setVolume(1, log=False)
    sound_5_M.setSound(S5, secs=0.25, hamming=True)
    sound_5_M.setVolume(1, log=False)
    sound_6_M.setSound(S6, secs=0.25, hamming=True)
    sound_6_M.setVolume(1, log=False)
    sound_7_M.setSound(S7, secs=0.25, hamming=True)
    sound_7_M.setVolume(1, log=False)
    sound_8_M.setSound(S8, secs=0.25, hamming=True)
    sound_8_M.setVolume(1, log=False)
    sound_9_M.setSound(S9, secs=0.25, hamming=True)
    sound_9_M.setVolume(1, log=False)
    sound_10_M.setSound(S10, secs=0.25, hamming=True)
    sound_10_M.setVolume(1, log=False)
    sound_11_M.setSound(S11, secs=0.25, hamming=True)
    sound_11_M.setVolume(1, log=False)
    sound_12_M.setSound(S12, secs=0.25, hamming=True)
    sound_12_M.setVolume(1, log=False)
    sound_13_M.setSound(S13, secs=0.25, hamming=True)
    sound_13_M.setVolume(1, log=False)
    sound_14_M.setSound(S14, secs=0.25, hamming=True)
    sound_14_M.setVolume(1, log=False)
    sound_15_M.setSound(S15, secs=0.25, hamming=True)
    sound_15_M.setVolume(1, log=False)
    sound_16_M.setSound(S16, secs=0.25, hamming=True)
    sound_16_M.setVolume(1, log=False)
    rating_2.reset()
    # keep track of which components have finished
    trial_IOI_M_250Components = [sound_1_M, sound_2_M, sound_3_M, sound_4_M, sound_5_M, sound_6_M, sound_7_M, sound_8_M, sound_9_M, sound_10_M, sound_11_M, sound_12_M, sound_13_M, sound_14_M, sound_15_M, sound_16_M, HowManyMelodies_IOI_M, rating_2]
    for thisComponent in trial_IOI_M_250Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_IOI_M_250Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_IOI_M_250"-------
    while continueRoutine:
        # get current time
        t = trial_IOI_M_250Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_IOI_M_250Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1_M
        if sound_1_M.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            sound_1_M.frameNStart = frameN  # exact frame index
            sound_1_M.tStart = t  # local t and not account for scr refresh
            sound_1_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1_M.play(when=win)  # sync with win flip
        if sound_1_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_1_M.tStop = t  # not accounting for scr refresh
                sound_1_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1_M, 'tStopRefresh')  # time at next scr refresh
                sound_1_M.stop()
        # start/stop sound_2_M
        if sound_2_M.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            sound_2_M.frameNStart = frameN  # exact frame index
            sound_2_M.tStart = t  # local t and not account for scr refresh
            sound_2_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2_M.play(when=win)  # sync with win flip
        if sound_2_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_2_M.tStop = t  # not accounting for scr refresh
                sound_2_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2_M, 'tStopRefresh')  # time at next scr refresh
                sound_2_M.stop()
        # start/stop sound_3_M
        if sound_3_M.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            sound_3_M.frameNStart = frameN  # exact frame index
            sound_3_M.tStart = t  # local t and not account for scr refresh
            sound_3_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_3_M.play(when=win)  # sync with win flip
        if sound_3_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_3_M.tStop = t  # not accounting for scr refresh
                sound_3_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_3_M, 'tStopRefresh')  # time at next scr refresh
                sound_3_M.stop()
        # start/stop sound_4_M
        if sound_4_M.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            sound_4_M.frameNStart = frameN  # exact frame index
            sound_4_M.tStart = t  # local t and not account for scr refresh
            sound_4_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_4_M.play(when=win)  # sync with win flip
        if sound_4_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_4_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_4_M.tStop = t  # not accounting for scr refresh
                sound_4_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_4_M, 'tStopRefresh')  # time at next scr refresh
                sound_4_M.stop()
        # start/stop sound_5_M
        if sound_5_M.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            sound_5_M.frameNStart = frameN  # exact frame index
            sound_5_M.tStart = t  # local t and not account for scr refresh
            sound_5_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_5_M.play(when=win)  # sync with win flip
        if sound_5_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_5_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_5_M.tStop = t  # not accounting for scr refresh
                sound_5_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_5_M, 'tStopRefresh')  # time at next scr refresh
                sound_5_M.stop()
        # start/stop sound_6_M
        if sound_6_M.status == NOT_STARTED and tThisFlip >= 1.75-frameTolerance:
            # keep track of start time/frame for later
            sound_6_M.frameNStart = frameN  # exact frame index
            sound_6_M.tStart = t  # local t and not account for scr refresh
            sound_6_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_6_M.play(when=win)  # sync with win flip
        if sound_6_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_6_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_6_M.tStop = t  # not accounting for scr refresh
                sound_6_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_6_M, 'tStopRefresh')  # time at next scr refresh
                sound_6_M.stop()
        # start/stop sound_7_M
        if sound_7_M.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            sound_7_M.frameNStart = frameN  # exact frame index
            sound_7_M.tStart = t  # local t and not account for scr refresh
            sound_7_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_7_M.play(when=win)  # sync with win flip
        if sound_7_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_7_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_7_M.tStop = t  # not accounting for scr refresh
                sound_7_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_7_M, 'tStopRefresh')  # time at next scr refresh
                sound_7_M.stop()
        # start/stop sound_8_M
        if sound_8_M.status == NOT_STARTED and tThisFlip >= 2.25-frameTolerance:
            # keep track of start time/frame for later
            sound_8_M.frameNStart = frameN  # exact frame index
            sound_8_M.tStart = t  # local t and not account for scr refresh
            sound_8_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_8_M.play(when=win)  # sync with win flip
        if sound_8_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_8_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_8_M.tStop = t  # not accounting for scr refresh
                sound_8_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_8_M, 'tStopRefresh')  # time at next scr refresh
                sound_8_M.stop()
        # start/stop sound_9_M
        if sound_9_M.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            sound_9_M.frameNStart = frameN  # exact frame index
            sound_9_M.tStart = t  # local t and not account for scr refresh
            sound_9_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_9_M.play(when=win)  # sync with win flip
        if sound_9_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_9_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_9_M.tStop = t  # not accounting for scr refresh
                sound_9_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_9_M, 'tStopRefresh')  # time at next scr refresh
                sound_9_M.stop()
        # start/stop sound_10_M
        if sound_10_M.status == NOT_STARTED and tThisFlip >= 2.75-frameTolerance:
            # keep track of start time/frame for later
            sound_10_M.frameNStart = frameN  # exact frame index
            sound_10_M.tStart = t  # local t and not account for scr refresh
            sound_10_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_10_M.play(when=win)  # sync with win flip
        if sound_10_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_10_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_10_M.tStop = t  # not accounting for scr refresh
                sound_10_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_10_M, 'tStopRefresh')  # time at next scr refresh
                sound_10_M.stop()
        # start/stop sound_11_M
        if sound_11_M.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            sound_11_M.frameNStart = frameN  # exact frame index
            sound_11_M.tStart = t  # local t and not account for scr refresh
            sound_11_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_11_M.play(when=win)  # sync with win flip
        if sound_11_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_11_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_11_M.tStop = t  # not accounting for scr refresh
                sound_11_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_11_M, 'tStopRefresh')  # time at next scr refresh
                sound_11_M.stop()
        # start/stop sound_12_M
        if sound_12_M.status == NOT_STARTED and tThisFlip >= 3.25-frameTolerance:
            # keep track of start time/frame for later
            sound_12_M.frameNStart = frameN  # exact frame index
            sound_12_M.tStart = t  # local t and not account for scr refresh
            sound_12_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_12_M.play(when=win)  # sync with win flip
        if sound_12_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_12_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_12_M.tStop = t  # not accounting for scr refresh
                sound_12_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_12_M, 'tStopRefresh')  # time at next scr refresh
                sound_12_M.stop()
        # start/stop sound_13_M
        if sound_13_M.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            sound_13_M.frameNStart = frameN  # exact frame index
            sound_13_M.tStart = t  # local t and not account for scr refresh
            sound_13_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_13_M.play(when=win)  # sync with win flip
        if sound_13_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_13_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_13_M.tStop = t  # not accounting for scr refresh
                sound_13_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_13_M, 'tStopRefresh')  # time at next scr refresh
                sound_13_M.stop()
        # start/stop sound_14_M
        if sound_14_M.status == NOT_STARTED and tThisFlip >= 3.75-frameTolerance:
            # keep track of start time/frame for later
            sound_14_M.frameNStart = frameN  # exact frame index
            sound_14_M.tStart = t  # local t and not account for scr refresh
            sound_14_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_14_M.play(when=win)  # sync with win flip
        if sound_14_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_14_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_14_M.tStop = t  # not accounting for scr refresh
                sound_14_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_14_M, 'tStopRefresh')  # time at next scr refresh
                sound_14_M.stop()
        # start/stop sound_15_M
        if sound_15_M.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            sound_15_M.frameNStart = frameN  # exact frame index
            sound_15_M.tStart = t  # local t and not account for scr refresh
            sound_15_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_15_M.play(when=win)  # sync with win flip
        if sound_15_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_15_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_15_M.tStop = t  # not accounting for scr refresh
                sound_15_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_15_M, 'tStopRefresh')  # time at next scr refresh
                sound_15_M.stop()
        # start/stop sound_16_M
        if sound_16_M.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
            # keep track of start time/frame for later
            sound_16_M.frameNStart = frameN  # exact frame index
            sound_16_M.tStart = t  # local t and not account for scr refresh
            sound_16_M.tStartRefresh = tThisFlipGlobal  # on global time
            sound_16_M.play(when=win)  # sync with win flip
        if sound_16_M.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_16_M.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_16_M.tStop = t  # not accounting for scr refresh
                sound_16_M.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_16_M, 'tStopRefresh')  # time at next scr refresh
                sound_16_M.stop()
        
        # *HowManyMelodies_IOI_M* updates
        if HowManyMelodies_IOI_M.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HowManyMelodies_IOI_M.frameNStart = frameN  # exact frame index
            HowManyMelodies_IOI_M.tStart = t  # local t and not account for scr refresh
            HowManyMelodies_IOI_M.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HowManyMelodies_IOI_M, 'tStartRefresh')  # time at next scr refresh
            HowManyMelodies_IOI_M.setAutoDraw(True)
        # *rating_2* updates
        if rating_2.status == NOT_STARTED and t >= 4.75-frameTolerance:
            # keep track of start time/frame for later
            rating_2.frameNStart = frameN  # exact frame index
            rating_2.tStart = t  # local t and not account for scr refresh
            rating_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_2, 'tStartRefresh')  # time at next scr refresh
            rating_2.setAutoDraw(True)
        continueRoutine &= rating_2.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_IOI_M_250Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_IOI_M_250"-------
    for thisComponent in trial_IOI_M_250Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_1_M.started', sound_1_M.tStartRefresh)
    IOI_M.addData('sound_1_M.stopped', sound_1_M.tStopRefresh)
    sound_2_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_2_M.started', sound_2_M.tStartRefresh)
    IOI_M.addData('sound_2_M.stopped', sound_2_M.tStopRefresh)
    sound_3_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_3_M.started', sound_3_M.tStartRefresh)
    IOI_M.addData('sound_3_M.stopped', sound_3_M.tStopRefresh)
    sound_4_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_4_M.started', sound_4_M.tStartRefresh)
    IOI_M.addData('sound_4_M.stopped', sound_4_M.tStopRefresh)
    sound_5_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_5_M.started', sound_5_M.tStartRefresh)
    IOI_M.addData('sound_5_M.stopped', sound_5_M.tStopRefresh)
    sound_6_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_6_M.started', sound_6_M.tStartRefresh)
    IOI_M.addData('sound_6_M.stopped', sound_6_M.tStopRefresh)
    sound_7_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_7_M.started', sound_7_M.tStartRefresh)
    IOI_M.addData('sound_7_M.stopped', sound_7_M.tStopRefresh)
    sound_8_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_8_M.started', sound_8_M.tStartRefresh)
    IOI_M.addData('sound_8_M.stopped', sound_8_M.tStopRefresh)
    sound_9_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_9_M.started', sound_9_M.tStartRefresh)
    IOI_M.addData('sound_9_M.stopped', sound_9_M.tStopRefresh)
    sound_10_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_10_M.started', sound_10_M.tStartRefresh)
    IOI_M.addData('sound_10_M.stopped', sound_10_M.tStopRefresh)
    sound_11_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_11_M.started', sound_11_M.tStartRefresh)
    IOI_M.addData('sound_11_M.stopped', sound_11_M.tStopRefresh)
    sound_12_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_12_M.started', sound_12_M.tStartRefresh)
    IOI_M.addData('sound_12_M.stopped', sound_12_M.tStopRefresh)
    sound_13_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_13_M.started', sound_13_M.tStartRefresh)
    IOI_M.addData('sound_13_M.stopped', sound_13_M.tStopRefresh)
    sound_14_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_14_M.started', sound_14_M.tStartRefresh)
    IOI_M.addData('sound_14_M.stopped', sound_14_M.tStopRefresh)
    sound_15_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_15_M.started', sound_15_M.tStartRefresh)
    IOI_M.addData('sound_15_M.stopped', sound_15_M.tStopRefresh)
    sound_16_M.stop()  # ensure sound has stopped at end of routine
    IOI_M.addData('sound_16_M.started', sound_16_M.tStartRefresh)
    IOI_M.addData('sound_16_M.stopped', sound_16_M.tStopRefresh)
    IOI_M.addData('HowManyMelodies_IOI_M.started', HowManyMelodies_IOI_M.tStartRefresh)
    IOI_M.addData('HowManyMelodies_IOI_M.stopped', HowManyMelodies_IOI_M.tStopRefresh)
    # store data for IOI_M (TrialHandler)
    IOI_M.addData('rating_2.response', rating_2.getRating())
    IOI_M.addData('rating_2.rt', rating_2.getRT())
    IOI_M.addData('rating_2.history', rating_2.getHistory())
    IOI_M.addData('rating_2.started', rating_2.tStart)
    IOI_M.addData('rating_2.stopped', rating_2.tStop)
    # the Routine "trial_IOI_M_250" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'IOI_M'


# set up handler to look after randomisation of conditions etc
IOI_S = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('IOI_S.xlsx'),
    seed=None, name='IOI_S')
thisExp.addLoop(IOI_S)  # add the loop to the experiment
thisIOI_S = IOI_S.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIOI_S.rgb)
if thisIOI_S != None:
    for paramName in thisIOI_S:
        exec('{} = thisIOI_S[paramName]'.format(paramName))

for thisIOI_S in IOI_S:
    currentLoop = IOI_S
    # abbreviate parameter names if possible (e.g. rgb = thisIOI_S.rgb)
    if thisIOI_S != None:
        for paramName in thisIOI_S:
            exec('{} = thisIOI_S[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_IOI_S_125"-------
    # update component parameters for each repeat
    sound_1_S.setSound(S1, secs=0.125, hamming=True)
    sound_1_S.setVolume(1, log=False)
    sound_2_S.setSound(S2, secs=0.125, hamming=True)
    sound_2_S.setVolume(1, log=False)
    sound_3_S.setSound(S3, secs=0.125, hamming=True)
    sound_3_S.setVolume(1, log=False)
    sound_4_S.setSound(S4, secs=0.125, hamming=True)
    sound_4_S.setVolume(1, log=False)
    sound_5_S.setSound(S5, secs=0.125, hamming=True)
    sound_5_S.setVolume(1, log=False)
    sound_6_S.setSound(S6, secs=0.125, hamming=True)
    sound_6_S.setVolume(1, log=False)
    sound_7_S.setSound(S7, secs=0.125, hamming=True)
    sound_7_S.setVolume(1, log=False)
    sound_8_S.setSound(S8, secs=0.125, hamming=True)
    sound_8_S.setVolume(1, log=False)
    sound_9_S.setSound(S9, secs=0.125, hamming=True)
    sound_9_S.setVolume(1, log=False)
    sound_10_S.setSound(S10, secs=0.125, hamming=True)
    sound_10_S.setVolume(1, log=False)
    sound_11_S.setSound(S11, secs=0.125, hamming=True)
    sound_11_S.setVolume(1, log=False)
    sound_12_S.setSound(S12, secs=0.125, hamming=False)
    sound_12_S.setVolume(1, log=False)
    sound_13_S.setSound(S13, secs=0.125, hamming=True)
    sound_13_S.setVolume(1, log=False)
    sound_14_S.setSound(S14, secs=0.125, hamming=True)
    sound_14_S.setVolume(1, log=False)
    sound_15_S.setSound(S15, secs=0.125, hamming=True)
    sound_15_S.setVolume(1, log=False)
    sound_16_S.setSound(S16, secs=0.125, hamming=True)
    sound_16_S.setVolume(1, log=False)
    rating_3.reset()
    # keep track of which components have finished
    trial_IOI_S_125Components = [sound_1_S, sound_2_S, sound_3_S, sound_4_S, sound_5_S, sound_6_S, sound_7_S, sound_8_S, sound_9_S, sound_10_S, sound_11_S, sound_12_S, sound_13_S, sound_14_S, sound_15_S, sound_16_S, HowManyMelodies_IOI_S, rating_3]
    for thisComponent in trial_IOI_S_125Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_IOI_S_125Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_IOI_S_125"-------
    while continueRoutine:
        # get current time
        t = trial_IOI_S_125Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_IOI_S_125Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1_S
        if sound_1_S.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            sound_1_S.frameNStart = frameN  # exact frame index
            sound_1_S.tStart = t  # local t and not account for scr refresh
            sound_1_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1_S.play(when=win)  # sync with win flip
        if sound_1_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_1_S.tStop = t  # not accounting for scr refresh
                sound_1_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1_S, 'tStopRefresh')  # time at next scr refresh
                sound_1_S.stop()
        # start/stop sound_2_S
        if sound_2_S.status == NOT_STARTED and tThisFlip >= 0.625-frameTolerance:
            # keep track of start time/frame for later
            sound_2_S.frameNStart = frameN  # exact frame index
            sound_2_S.tStart = t  # local t and not account for scr refresh
            sound_2_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2_S.play(when=win)  # sync with win flip
        if sound_2_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_2_S.tStop = t  # not accounting for scr refresh
                sound_2_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2_S, 'tStopRefresh')  # time at next scr refresh
                sound_2_S.stop()
        # start/stop sound_3_S
        if sound_3_S.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            sound_3_S.frameNStart = frameN  # exact frame index
            sound_3_S.tStart = t  # local t and not account for scr refresh
            sound_3_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_3_S.play(when=win)  # sync with win flip
        if sound_3_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_3_S.tStop = t  # not accounting for scr refresh
                sound_3_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_3_S, 'tStopRefresh')  # time at next scr refresh
                sound_3_S.stop()
        # start/stop sound_4_S
        if sound_4_S.status == NOT_STARTED and tThisFlip >= 0.875-frameTolerance:
            # keep track of start time/frame for later
            sound_4_S.frameNStart = frameN  # exact frame index
            sound_4_S.tStart = t  # local t and not account for scr refresh
            sound_4_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_4_S.play(when=win)  # sync with win flip
        if sound_4_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_4_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_4_S.tStop = t  # not accounting for scr refresh
                sound_4_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_4_S, 'tStopRefresh')  # time at next scr refresh
                sound_4_S.stop()
        # start/stop sound_5_S
        if sound_5_S.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            sound_5_S.frameNStart = frameN  # exact frame index
            sound_5_S.tStart = t  # local t and not account for scr refresh
            sound_5_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_5_S.play(when=win)  # sync with win flip
        if sound_5_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_5_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_5_S.tStop = t  # not accounting for scr refresh
                sound_5_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_5_S, 'tStopRefresh')  # time at next scr refresh
                sound_5_S.stop()
        # start/stop sound_6_S
        if sound_6_S.status == NOT_STARTED and tThisFlip >= 1.125-frameTolerance:
            # keep track of start time/frame for later
            sound_6_S.frameNStart = frameN  # exact frame index
            sound_6_S.tStart = t  # local t and not account for scr refresh
            sound_6_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_6_S.play(when=win)  # sync with win flip
        if sound_6_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_6_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_6_S.tStop = t  # not accounting for scr refresh
                sound_6_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_6_S, 'tStopRefresh')  # time at next scr refresh
                sound_6_S.stop()
        # start/stop sound_7_S
        if sound_7_S.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            sound_7_S.frameNStart = frameN  # exact frame index
            sound_7_S.tStart = t  # local t and not account for scr refresh
            sound_7_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_7_S.play(when=win)  # sync with win flip
        if sound_7_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_7_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_7_S.tStop = t  # not accounting for scr refresh
                sound_7_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_7_S, 'tStopRefresh')  # time at next scr refresh
                sound_7_S.stop()
        # start/stop sound_8_S
        if sound_8_S.status == NOT_STARTED and tThisFlip >= 1.375-frameTolerance:
            # keep track of start time/frame for later
            sound_8_S.frameNStart = frameN  # exact frame index
            sound_8_S.tStart = t  # local t and not account for scr refresh
            sound_8_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_8_S.play(when=win)  # sync with win flip
        if sound_8_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_8_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_8_S.tStop = t  # not accounting for scr refresh
                sound_8_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_8_S, 'tStopRefresh')  # time at next scr refresh
                sound_8_S.stop()
        # start/stop sound_9_S
        if sound_9_S.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            sound_9_S.frameNStart = frameN  # exact frame index
            sound_9_S.tStart = t  # local t and not account for scr refresh
            sound_9_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_9_S.play(when=win)  # sync with win flip
        if sound_9_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_9_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_9_S.tStop = t  # not accounting for scr refresh
                sound_9_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_9_S, 'tStopRefresh')  # time at next scr refresh
                sound_9_S.stop()
        # start/stop sound_10_S
        if sound_10_S.status == NOT_STARTED and tThisFlip >= 1.625-frameTolerance:
            # keep track of start time/frame for later
            sound_10_S.frameNStart = frameN  # exact frame index
            sound_10_S.tStart = t  # local t and not account for scr refresh
            sound_10_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_10_S.play(when=win)  # sync with win flip
        if sound_10_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_10_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_10_S.tStop = t  # not accounting for scr refresh
                sound_10_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_10_S, 'tStopRefresh')  # time at next scr refresh
                sound_10_S.stop()
        # start/stop sound_11_S
        if sound_11_S.status == NOT_STARTED and tThisFlip >= 1.75-frameTolerance:
            # keep track of start time/frame for later
            sound_11_S.frameNStart = frameN  # exact frame index
            sound_11_S.tStart = t  # local t and not account for scr refresh
            sound_11_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_11_S.play(when=win)  # sync with win flip
        if sound_11_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_11_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_11_S.tStop = t  # not accounting for scr refresh
                sound_11_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_11_S, 'tStopRefresh')  # time at next scr refresh
                sound_11_S.stop()
        # start/stop sound_12_S
        if sound_12_S.status == NOT_STARTED and tThisFlip >= 1.875-frameTolerance:
            # keep track of start time/frame for later
            sound_12_S.frameNStart = frameN  # exact frame index
            sound_12_S.tStart = t  # local t and not account for scr refresh
            sound_12_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_12_S.play(when=win)  # sync with win flip
        if sound_12_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_12_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_12_S.tStop = t  # not accounting for scr refresh
                sound_12_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_12_S, 'tStopRefresh')  # time at next scr refresh
                sound_12_S.stop()
        # start/stop sound_13_S
        if sound_13_S.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            sound_13_S.frameNStart = frameN  # exact frame index
            sound_13_S.tStart = t  # local t and not account for scr refresh
            sound_13_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_13_S.play(when=win)  # sync with win flip
        if sound_13_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_13_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_13_S.tStop = t  # not accounting for scr refresh
                sound_13_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_13_S, 'tStopRefresh')  # time at next scr refresh
                sound_13_S.stop()
        # start/stop sound_14_S
        if sound_14_S.status == NOT_STARTED and tThisFlip >= 2.125-frameTolerance:
            # keep track of start time/frame for later
            sound_14_S.frameNStart = frameN  # exact frame index
            sound_14_S.tStart = t  # local t and not account for scr refresh
            sound_14_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_14_S.play(when=win)  # sync with win flip
        if sound_14_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_14_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_14_S.tStop = t  # not accounting for scr refresh
                sound_14_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_14_S, 'tStopRefresh')  # time at next scr refresh
                sound_14_S.stop()
        # start/stop sound_15_S
        if sound_15_S.status == NOT_STARTED and tThisFlip >= 2.25-frameTolerance:
            # keep track of start time/frame for later
            sound_15_S.frameNStart = frameN  # exact frame index
            sound_15_S.tStart = t  # local t and not account for scr refresh
            sound_15_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_15_S.play(when=win)  # sync with win flip
        if sound_15_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_15_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_15_S.tStop = t  # not accounting for scr refresh
                sound_15_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_15_S, 'tStopRefresh')  # time at next scr refresh
                sound_15_S.stop()
        # start/stop sound_16_S
        if sound_16_S.status == NOT_STARTED and tThisFlip >= 2.375-frameTolerance:
            # keep track of start time/frame for later
            sound_16_S.frameNStart = frameN  # exact frame index
            sound_16_S.tStart = t  # local t and not account for scr refresh
            sound_16_S.tStartRefresh = tThisFlipGlobal  # on global time
            sound_16_S.play(when=win)  # sync with win flip
        if sound_16_S.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_16_S.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                sound_16_S.tStop = t  # not accounting for scr refresh
                sound_16_S.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_16_S, 'tStopRefresh')  # time at next scr refresh
                sound_16_S.stop()
        
        # *HowManyMelodies_IOI_S* updates
        if HowManyMelodies_IOI_S.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HowManyMelodies_IOI_S.frameNStart = frameN  # exact frame index
            HowManyMelodies_IOI_S.tStart = t  # local t and not account for scr refresh
            HowManyMelodies_IOI_S.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HowManyMelodies_IOI_S, 'tStartRefresh')  # time at next scr refresh
            HowManyMelodies_IOI_S.setAutoDraw(True)
        # *rating_3* updates
        if rating_3.status == NOT_STARTED and t >= 2.625-frameTolerance:
            # keep track of start time/frame for later
            rating_3.frameNStart = frameN  # exact frame index
            rating_3.tStart = t  # local t and not account for scr refresh
            rating_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_3, 'tStartRefresh')  # time at next scr refresh
            rating_3.setAutoDraw(True)
        continueRoutine &= rating_3.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_IOI_S_125Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_IOI_S_125"-------
    for thisComponent in trial_IOI_S_125Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_1_S.started', sound_1_S.tStartRefresh)
    IOI_S.addData('sound_1_S.stopped', sound_1_S.tStopRefresh)
    sound_2_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_2_S.started', sound_2_S.tStartRefresh)
    IOI_S.addData('sound_2_S.stopped', sound_2_S.tStopRefresh)
    sound_3_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_3_S.started', sound_3_S.tStartRefresh)
    IOI_S.addData('sound_3_S.stopped', sound_3_S.tStopRefresh)
    sound_4_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_4_S.started', sound_4_S.tStartRefresh)
    IOI_S.addData('sound_4_S.stopped', sound_4_S.tStopRefresh)
    sound_5_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_5_S.started', sound_5_S.tStartRefresh)
    IOI_S.addData('sound_5_S.stopped', sound_5_S.tStopRefresh)
    sound_6_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_6_S.started', sound_6_S.tStartRefresh)
    IOI_S.addData('sound_6_S.stopped', sound_6_S.tStopRefresh)
    sound_7_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_7_S.started', sound_7_S.tStartRefresh)
    IOI_S.addData('sound_7_S.stopped', sound_7_S.tStopRefresh)
    sound_8_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_8_S.started', sound_8_S.tStartRefresh)
    IOI_S.addData('sound_8_S.stopped', sound_8_S.tStopRefresh)
    sound_9_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_9_S.started', sound_9_S.tStartRefresh)
    IOI_S.addData('sound_9_S.stopped', sound_9_S.tStopRefresh)
    sound_10_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_10_S.started', sound_10_S.tStartRefresh)
    IOI_S.addData('sound_10_S.stopped', sound_10_S.tStopRefresh)
    sound_11_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_11_S.started', sound_11_S.tStartRefresh)
    IOI_S.addData('sound_11_S.stopped', sound_11_S.tStopRefresh)
    sound_12_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_12_S.started', sound_12_S.tStartRefresh)
    IOI_S.addData('sound_12_S.stopped', sound_12_S.tStopRefresh)
    sound_13_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_13_S.started', sound_13_S.tStartRefresh)
    IOI_S.addData('sound_13_S.stopped', sound_13_S.tStopRefresh)
    sound_14_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_14_S.started', sound_14_S.tStartRefresh)
    IOI_S.addData('sound_14_S.stopped', sound_14_S.tStopRefresh)
    sound_15_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_15_S.started', sound_15_S.tStartRefresh)
    IOI_S.addData('sound_15_S.stopped', sound_15_S.tStopRefresh)
    sound_16_S.stop()  # ensure sound has stopped at end of routine
    IOI_S.addData('sound_16_S.started', sound_16_S.tStartRefresh)
    IOI_S.addData('sound_16_S.stopped', sound_16_S.tStopRefresh)
    IOI_S.addData('HowManyMelodies_IOI_S.started', HowManyMelodies_IOI_S.tStartRefresh)
    IOI_S.addData('HowManyMelodies_IOI_S.stopped', HowManyMelodies_IOI_S.tStopRefresh)
    # store data for IOI_S (TrialHandler)
    IOI_S.addData('rating_3.response', rating_3.getRating())
    IOI_S.addData('rating_3.rt', rating_3.getRT())
    IOI_S.addData('rating_3.history', rating_3.getHistory())
    IOI_S.addData('rating_3.started', rating_3.tStart)
    IOI_S.addData('rating_3.stopped', rating_3.tStop)
    # the Routine "trial_IOI_S_125" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'IOI_S'


# ------Prepare to start Routine "Finished"-------
# update component parameters for each repeat
# keep track of which components have finished
FinishedComponents = [text_3]
for thisComponent in FinishedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FinishedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Finished"-------
while continueRoutine:
    # get current time
    t = FinishedClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FinishedClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinishedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Finished"-------
for thisComponent in FinishedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "Finished" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
