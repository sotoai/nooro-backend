//
//  ContentView.swift
//  soto
//
//  Created by Joshua Soto on 3/27/25.
//
import SwiftUI

struct AgentCarouselView: View {
    @State private var agents = [
        Agent(name: "Ron", title: "THE BUILDER", imageName: "ron", isSpeaking: true, voiceID: "qNkzaJoHLLdpvgh5tISm"),
        Agent(name: "Leslie", title: "THE ACCELERATOR", imageName: "leslie", isSpeaking: false, voiceID: "vlS1ohKzOkKzVrkOUAOG"),
        Agent(name: "Ben", title: "THE MAPMAKER", imageName: "ben", isSpeaking: false, voiceID: "UgBBYS2sOqTuMpoF3BR0"),
        Agent(name: "Ann", title: "THE BRIDGE", imageName: "ann", isSpeaking: false, voiceID: "ESELSAYNsoxwNZeqEklA"),
        Agent(name: "Jerry", title: "THE REMEMBERER", imageName: "jerry", isSpeaking: false, voiceID: "goT3UYdM9bhm0n2lmKQx"),
        Agent(name: "Chris", title: "THE LENS", imageName: "chris", isSpeaking: false, voiceID: "Q4oILuo4P8VeXtE6FMLI"),
        Agent(name: "April", title: "THE WATCHER", imageName: "april", isSpeaking: false, voiceID: "SaqYcK3ZpDKBAImA8AdW"),
        Agent(name: "Tom", title: "THE VOICE", imageName: "tom", isSpeaking: false, voiceID: "yl2ZDV1MzN4HbQJbMihG"),
        Agent(name: "Donna", title: "THE STEWARD", imageName: "donna", isSpeaking: false, voiceID: "OOk3INdXVLRmSaQoAX9D")
    ]

    var body: some View {
        #if os(iOS)
        TabView {
            ForEach(agents.indices, id: \.self) { index in
                AgentChatView(agent: $agents[index])
            }
        }
        .tabViewStyle(PageTabViewStyle(indexDisplayMode: .never))
        #else
        ScrollView(.horizontal) {
            HStack(spacing: 0) {
                ForEach(agents.indices, id: \.self) { index in
                    AgentChatView(agent: $agents[index])
                        .frame(width: 500)
                }
            }
        }
        #endif
    }
}
