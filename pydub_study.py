# -*- coding: utf-8 -*-
# @Time    : 19-1-11 上午9:29
# @Author  : Felix Wang

# 需要安装 ffmpeg

from pydub import AudioSegment # pip install pydub

sound=AudioSegment.from_file("aaa.mp3","mp3")
sound2=AudioSegment.from_file('bbb.mp3','mp3')
# 把一个多声道音频分解成两个单声道
# index[0]为左声道
# index[1]为右声道
# sounds=sound.split_to_mono()
# print(sounds)


# 将两个单声道合并成多声道
# stereo_sound = AudioSegment.from_mono_audiosegments(sounds[0], sounds[1])



# # 取得音频的分贝数
# loudness = sound.dBFS
# print(loudness)
# # 获取音频音量大小，该值通常用来计算分贝数（dB= 20×lgX）
# loudness = sound.rms
# print(loudness)
# # 取得音频的声道数
# channel_count = sound.channels
# print(channel_count)
# # 取得音频文件采样宽度
# bytes_per_sample = sound.sample_width
# print(bytes_per_sample)
#
# # 取得音频文件采样频率
# frames_per_second = sound.frame_rate
# print(frames_per_second)
# #取得音频文件帧宽度
# bytes_per_frame = sound.frame_width
# print(bytes_per_frame)
#
# #取得音频中的最大振幅
# normalized_sound = sound.apply_gain(-sound.max_dBFS)
# print(normalized_sound)
# #取得音频的持续时间，同 len()
# print(sound.duration_seconds)
# print((len(sound) / 1000.0))
# #取得音频数据
# raw_audio_data = sound.raw_data
# # print(raw_audio_data)
# #取得音频的frame数量
# number_of_frames_in_sound = sound.frame_count()
# number_of_frames_in_200ms_of_sound = sound.frame_count(ms=200)
# print(number_of_frames_in_sound)
# print(number_of_frames_in_200ms_of_sound)

# 拼接sound1与sound2，返回一个新的AudioSegment实例
# cossfade：交叉渐变间隔 ms
# no_crossfade1 = sound.append(sound2, crossfade=5000)
# print(no_crossfade1)
# no_crossfade1.export(r'cc.wav',format='wav') # 输出

# 把sound2覆盖在sound1上，两个音频文件会叠加，如果sound2较长，则会被截断。
# 参数：
# position：覆盖起始位置（毫秒）
# loop：是否循环覆盖（true/false）
# times：重复覆盖次数（默认1）
# gain_during_overlay：调整被覆盖音频的音量（eg，-6.0）
# played_togther = sound.overlay(sound2)
# # sound2_starts_after_delay = sound.overlay(sound2, position=5000)
# # volume_of_sound1_reduced_during_overlay = sound.overlay(sound2, gain_during_overlay=-8)
# # sound2_repeats_until_sound1_ends = sound.overlay(sound2, loop=True)
# # sound2_plays_twice = sound.overlay(sound2, times=2)
# played_togther.export(r'dd.wav',format='wav') # 输出



#调整音量大小
# louder_via_method = sound.apply_gain(+3.5) # 提高
# quieter_via_method = sound.apply_gain(-5.7) # 减小


#淡出
# 参数：
# to_gain：淡出结束时音频音量下降到的分贝数
# from_gain：设置淡出前的所有音频分贝数
# start：淡出的起始位置
# end：淡出的结束位置
# duration：淡出持续时间
# fade_in_the_hard_way = sound.fade(from_gain=-120.0, start=0, duration=5000)
# fade_out_the_hard_way = sound.fade(to_gain=-120.0, end=0, duration=5000)

# 反向输出
# sound.reverse().export(r'ee.wav',format='wav') # 输出

# 调整多声道音频的左右声道音量
# 如果单声道音频调用此方法，它将先被转换为多声道
# stereo_balance_adjusted = sound.apply_gain_stereo(-6, +2)
#
# #左右声道平衡，按百分比增大一边，减小另一边
# # pan the sound 15% to the right
# panned_right = sound.pan(+0.15)
# # pan the sound 50% to the left
# panned_left = sound.pan(-0.50)
#
#
# # 基于DSP的渲染
# # 产生一个反向信号的副本，来消除反相位波，或者降低噪音
# sound.invert_phase()