# jabra-fade-in-disabler
Disable Jabra headset's volume fade-in feature

# The Problem
Jabra Evolve 65 headset has an annoying feature that fades in the volume of an audio stream, practically cutting off the beginning of every audio played. This requires rewinding the starting parts of videos in order to be able to hear the beginning. Worst of all, small notification pings are rendered completely inaudible since they are played out before Jabra's vaolume fade-in reaches an audible level. Root cause of this issue is not actually the headset but the Link adapter. (If the headset is connected using native BT, the issue goes away)

As of 14-July-2022, there is not way to disable this feature.

Customers have complained about this feature for more than two years on various forums online (including creating support tickets) but neither has the feature been disabled nor have they provided functionality to toggle it on/off.

References :
- [https://www.reddit.com/r/Jabra/comments/ihtr5g/evolve2_65_five_second_fade_in/](https://www.reddit.com/r/Jabra/comments/ihtr5g/evolve2_65_five_second_fade_in/)
- [https://www.reddit.com/r/Jabra/comments/k66whc/evolve2_85_audio_fade_in_out/](https://www.reddit.com/r/Jabra/comments/k66whc/evolve2_85_audio_fade_in_out/)
- [https://www.reddit.com/r/Jabra/comments/qowqmh/jabra_fading_in_and_out_i_am_about_to_return/](https://www.reddit.com/r/Jabra/comments/qowqmh/jabra_fading_in_and_out_i_am_about_to_return/)
- [https://www.reddit.com/r/Jabra/comments/n6eo3x/weird_fadein_issue_after_2_seconds_of_silence/](https://www.reddit.com/r/Jabra/comments/n6eo3x/weird_fadein_issue_after_2_seconds_of_silence/) 

# The Solution
As pointed out by some reddit threads, if a constant stream of volume audio is played in the background, the headset does not fade-in any new audio played on top.

The fade-in disabler app sits in your menu bar, detects the presence of a connected Jabra headset and plays a very an inauble audio signal in an infinite loop in the background. This cancels the fade-in behavior of the Jabra headset allowing you to enjoy uninterrupted audio.

# Current Limitations
- MacOS only (feel free to contribute a Windows version)