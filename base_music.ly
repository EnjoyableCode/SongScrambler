
\version "2.14.0"

\layout {
  \context {
    \Voice
    \remove "Note_heads_engraver"
    \consists "Completion_heads_engraver"
    \remove "Rest_engraver"
    \consists "Completion_rest_engraver"
  }
}

trackAchannelA = {


  \key c \major
    
  \tempo 4 = 120 
  
  
  \time 4/4 
  

  \key c \major
  
}

trackAchannelB = {
  
  \tempo 4 = 120 
  
  
  \time 4/4 
  

  \key c \major
  
}

trackAchannelC = {
  
  \tempo 4 = 120 
  
  
  \time 4/4 
  

  \key c \major
  
}

trackAchannelE = \relative c {
 \set midiInstrument = #"|||PUTINST1HERE|||"
  \voiceThree
|||PUTNOTESHERE1|||

}

trackAchannelG = \relative c {
  \set midiInstrument = #"|||PUTINST2HERE|||"
  \voiceOne
 |||PUTNOTESHERE2|||
}

trackAchannelI = \relative c {
 \set midiInstrument = #"|||PUTINST3HERE|||"
  \voiceFour
  |||PUTNOTESHERE3|||
}

trackA = <<

  \clef bass
  
  \context Voice = voiceA \trackAchannelA
  \context Voice = voiceB \trackAchannelB
  \context Voice = voiceC \trackAchannelC
  \context Voice = voiceD \trackAchannelE
  \context Voice = voiceE \trackAchannelG
  \context Voice = voiceF \trackAchannelI
>>


\score {
  <<
    \context Staff=trackA \trackA
  >>
  \layout {}
  \midi {
    \context {
      \Staff
      \remove "Staff_performer"
    }
    \context {
      \Voice
      \consists "Staff_performer"
    }
    \tempo 2 = 72
  }
}
