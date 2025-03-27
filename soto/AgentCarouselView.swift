//
//  ContentView.swift
//  soto
//
//  Created by Joshua Soto on 3/27/25.
//

import SwiftUI

struct AgentCarouselView: View {
    @State private var agents = [
        Agent(name: "Samantha", title: "PERSONAL ASSISTANT", imageName: "samantha", isSpeaking: true),
        Agent(name: "Driver", title: "THE ACCELERATOR", imageName: "driver", isSpeaking: false),
        Agent(name: "Strategist", title: "THE MAPMAKER", imageName: "strategist", isSpeaking: false)
    ]

    var body: some View {
        #if os(iOS)
        TabView {
            ForEach(agents.indices, id: \.self) { index in
                AgentChatView(agent: agents[index])
            }
        }
        .tabViewStyle(PageTabViewStyle(indexDisplayMode: .never))
        #else
        ScrollView(.horizontal) {
            HStack(spacing: 0) {
                ForEach(agents.indices, id: \.self) { index in
                    AgentChatView(agent: agents[index])
                        .frame(width: 500) // Set a fixed width per agent
                }
            }
        }
        #endif
    }
}
