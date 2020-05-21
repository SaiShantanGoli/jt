## meeting path
* greet
  - utter_greet
* schedule_a_meeting
  - action_a_meeting 
* meeting_time
  - action_a_meeting

## meeting path2
* schedule_a_meeting
  - action_a_meeting
* meeting_day
  - action_a_meeting

## meeting path3
* schedule_a_meeting
  - action_a_meeting
* meeting_day
  - action_a_meeting
* meeting_time
  - action_a_meeting

## meeting_path4
* schedule_a_meeting
  - action_a_meeting
* meeting_time
  - action_a_meeting
* meeting_day
  - action_a_meeting


<!---
* time_entry
  - utter_meeting_time
* output
  - utter_show_meeting_info
--->

## cancel meeting
* cancel_meeting
  - utter_cancel_meeting_info

## call issue
* my_call_is_dropping
  - utter_my_call_is_dropping_info

## mute all
* mute_all
  - utter_mute_all_info

## audio issue
* audio_not_clear
  - utter_audio_not_clear_info

## video issue
* video_is_buffering
  - utter_video_is_buffering_info

## screen share issue
* not_able_to_share_screen
  - utter_not_able_to_share_screen_info

## app issue
* jiomeet_not_working
  - utter_jiomeet_not_working_info

## meeting join
* join_a_meeting
  - utter_join_a_meeting_info
  - action_join_meeting

## meeting join path 2
* join_a_meeting
  - action_join_meeting
* id_of_meeting
  - action_join_meeting

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
