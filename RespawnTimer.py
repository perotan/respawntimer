#!/usr/bin/env python3

# Respawn Timer for GINA
# by Nekomimi <Manekineko>

import re
import csv

CATEGORY = 'RespawnTimer'
CSV = './RespawnTimeDB.csv'
DB = './RespawnTimeDB.xml'
TIMER = './RespawnTimer.xml'

def xml_header(trigger_group_name):
	xml = f'''\
<?xml version="1.0" encoding="utf-8"?>
<SharedData>
  <TriggerGroups>
    <TriggerGroup>
      <Name>{trigger_group_name}</Name>
      <Comments></Comments>
      <SelfCommented>False</SelfCommented>
      <GroupId>0</GroupId>
      <EnableByDefault>True</EnableByDefault>
      <TriggerGroups>
'''
	return(xml)

def tg_header(tg_name):
	xml = f'''\
        <TriggerGroup>
          <Name>{tg_name}</Name>
          <Comments></Comments>
          <SelfCommented>False</SelfCommented>
          <GroupId>0</GroupId>
          <EnableByDefault>True</EnableByDefault>
          <Triggers>
'''
	return(xml)

def trigger_db(zone_name, zone_id, timer):
	xml = f'''\
            <Trigger>
              <Name>{zone_id}</Name>
              <TriggerText>^(You have entered|There (is|are) \\d+ player(|s) in) {zone_name}\\.$</TriggerText>
              <Comments></Comments>
              <EnableRegex>True</EnableRegex>
              <UseText>False</UseText>
              <CopyToClipboard>False</CopyToClipboard>
              <ClipboardText></ClipboardText>
              <UseTextToVoice>False</UseTextToVoice>
              <InterruptSpeech>False</InterruptSpeech>
              <TextToVoiceText></TextToVoiceText>
              <PlayMediaFile>False</PlayMediaFile>
              <TimerType>Timer</TimerType>
              <TimerName>## {zone_id}: {timer}</TimerName>
              <RestartBasedOnTimerName>False</RestartBasedOnTimerName>
              <TimerMillisecondDuration></TimerMillisecondDuration>
              <TimerDuration>600</TimerDuration>
              <TimerVisibleDuration>0</TimerVisibleDuration>
              <TimerStartBehavior>RestartTimer</TimerStartBehavior>
              <TimerEndingTime>0</TimerEndingTime>
              <UseTimerEnding>False</UseTimerEnding>
              <UseTimerEnded>False</UseTimerEnded>
              <UseCounterResetTimer>False</UseCounterResetTimer>
              <CounterResetDuration>0</CounterResetDuration>
              <Category>{CATEGORY}</Category>
              <Modified>2021-06-15T00:00:00</Modified>
              <UseFastCheck>True</UseFastCheck>
              <TimerEarlyEnders>
                <EarlyEnder>
                  <EarlyEndText>^(You have entered|There (is|are) \\d+ player(|s) in) (?!.*{zone_name}).+$</EarlyEndText>
                  <EnableRegex>True</EnableRegex>
                </EarlyEnder>
              </TimerEarlyEnders>
            </Trigger>
'''
	return(xml)

def trigger_timer(timer):
	m1 = re.match(r'^(\d+):(\d+)$', timer)
	m2 = re.match(r'^(\d+)hours$', timer)
	if m1:
		timer_sec = (60 * int(m1.group(1))) + int(m1.group(2))
	elif m2:
		timer_sec = (60 * 60 * int(m2.group(1)))
	xml = f'''\
            <Trigger>
              <Name>{timer} slain</Name>
              <TriggerText>^(You have slain (.+)|(.+) has been slain by .+|{{C}} (##.*)(|!|\.))$</TriggerText>
              <Comments></Comments>
              <EnableRegex>True</EnableRegex>
              <UseText>False</UseText>
              <DisplayText></DisplayText>
              <CopyToClipboard>False</CopyToClipboard>
              <ClipboardText></ClipboardText>
              <UseTextToVoice>False</UseTextToVoice>
              <InterruptSpeech>False</InterruptSpeech>
              <TextToVoiceText></TextToVoiceText>
              <PlayMediaFile>False</PlayMediaFile>
              <TimerType>Timer</TimerType>
              <TimerName>${{2}}${{3}}${{4}}</TimerName>
              <RestartBasedOnTimerName>False</RestartBasedOnTimerName>
              <TimerMillisecondDuration></TimerMillisecondDuration>
              <TimerDuration>{timer_sec}</TimerDuration>
              <TimerVisibleDuration>0</TimerVisibleDuration>
              <TimerStartBehavior>StartNewTimer</TimerStartBehavior>
              <TimerEndingTime>30</TimerEndingTime>
              <UseTimerEnding>True</UseTimerEnding>
              <UseTimerEnded>False</UseTimerEnded>
              <TimerEndingTrigger>
                <UseText>True</UseText>
                <DisplayText>spawn soon</DisplayText>
                <UseTextToVoice>False</UseTextToVoice>
                <InterruptSpeech>False</InterruptSpeech>
                <TextToVoiceText></TextToVoiceText>
                <PlayMediaFile>False</PlayMediaFile>
              </TimerEndingTrigger>
              <UseCounterResetTimer>False</UseCounterResetTimer>
              <CounterResetDuration>0</CounterResetDuration>
              <Category>{CATEGORY}</Category>
              <Modified>2021-06-15T00:00:00</Modified>
              <UseFastCheck>True</UseFastCheck>
              <TimerEarlyEnders />
              <TimerEarlyEnders>
                <EarlyEnder>
                  <EarlyEndText>^{{C}} ##reset\\.$</EarlyEndText>
                  <EnableRegex>True</EnableRegex>
                </EarlyEnder>
              </TimerEarlyEnders>
            </Trigger>
            <Trigger>
              <Name>{timer} xp</Name>
              <TriggerText>^You gain (|party )experience!!$</TriggerText>
              <Comments></Comments>
              <EnableRegex>True</EnableRegex>
              <UseText>False</UseText>
              <DisplayText></DisplayText>
              <CopyToClipboard>False</CopyToClipboard>
              <ClipboardText></ClipboardText>
              <UseTextToVoice>False</UseTextToVoice>
              <InterruptSpeech>False</InterruptSpeech>
              <TextToVoiceText></TextToVoiceText>
              <PlayMediaFile>False</PlayMediaFile>
              <TimerType>Timer</TimerType>
              <TimerName>^^^^^</TimerName>
              <RestartBasedOnTimerName>False</RestartBasedOnTimerName>
              <TimerMillisecondDuration></TimerMillisecondDuration>
              <TimerDuration>{timer_sec}</TimerDuration>
              <TimerVisibleDuration>0</TimerVisibleDuration>
              <TimerStartBehavior>StartNewTimer</TimerStartBehavior>
              <TimerEndingTime>30</TimerEndingTime>
              <UseTimerEnding>True</UseTimerEnding>
              <UseTimerEnded>False</UseTimerEnded>
              <TimerEndingTrigger>
                <UseText>True</UseText>
                <DisplayText>spawn soon</DisplayText>
                <UseTextToVoice>False</UseTextToVoice>
                <InterruptSpeech>False</InterruptSpeech>
                <TextToVoiceText></TextToVoiceText>
                <PlayMediaFile>False</PlayMediaFile>
              </TimerEndingTrigger>
              <UseCounterResetTimer>False</UseCounterResetTimer>
              <CounterResetDuration>0</CounterResetDuration>
              <Category>{CATEGORY}</Category>
              <Modified>2021-06-15T00:00:00</Modified>
              <UseFastCheck>True</UseFastCheck>
              <TimerEarlyEnders />
              <TimerEarlyEnders>
                <EarlyEnder>
                  <EarlyEndText>^{{C}} ##reset\\.$</EarlyEndText>
                  <EnableRegex>True</EnableRegex>
                </EarlyEnder>
              </TimerEarlyEnders>
            </Trigger>
'''
	return(xml)

def tg_footer():
	xml = '''\
          </Triggers>
        </TriggerGroup>
'''
	return(xml)

def xml_footer():
	xml = '''\
      </TriggerGroups>
    </TriggerGroup>
  </TriggerGroups>
</SharedData>
'''
	return(xml)


if __name__ == "__main__":
	# read csv
	with open(CSV) as fi:
		reader = csv.reader(fi)
		zones = [row for row in reader]
	
	# write db	
	fo = open(DB, mode='w')
	fo.write(xml_header('Respawn Time DB'))
	region_cont = False
	for zone in zones:
		zone_name = zone[0]
		zone_id = zone[1]
		timer = zone[2]
		m1 = re.match(r'^REGION +(.+)', zone_name)
		if m1:
			region = m1.group(1)
			if region_cont:
				fo.write(tg_footer())
				fo.write(tg_header(region))
			else:
				fo.write(tg_header(region))
				region_cont = True
			continue
		else:
			fo.write(trigger_db(zone_name, zone_id, timer))
	fo.write(tg_footer())
	fo.write(xml_footer())
	fo.close()
	
	# write timer
	fo = open(TIMER, mode='w')
	fo.write(xml_header('Respawn Timer'))
	timers_m = []
	timers_h = []
	for zone in zones:
		timer = zone[2]
		find_h = re.findall(r'\d+hours', timer)
		find_m = re.findall(r'\d+:\d+', timer)
		if find_h:
			timers_h.extend([i for i in find_h])
			continue
		elif find_m:
			timers_m.extend([i for i in find_m])
	timers = sorted(list(set(timers_m))) + sorted(list(set(timers_h)))
	for time in timers:
		tg_time = time
		m1 = re.match(r'^\d+hours$', tg_time)
		if m1:
			tg_time = 'zzz ' + tg_time
		fo.write(tg_header(tg_time))
		fo.write(trigger_timer(time))
		fo.write(tg_footer())
	fo.write(xml_footer())
	fo.close()

