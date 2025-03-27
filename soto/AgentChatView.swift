import SwiftUI
import AVFoundation

struct Agent: Identifiable, Equatable {
    let id = UUID()
    let name: String
    let title: String
    let imageName: String
    var isSpeaking: Bool
    let voiceID: String
}

struct AgentChatView: View {
    @Binding var agent: Agent
    @State private var messages: [ChatMessage] = [
        ChatMessage(isFromUser: true, text: "Hi Sam. Can you please schedule some time with Mike Haro this coming Wednesday?"),
        ChatMessage(isFromUser: false, text: "Absolutely! Your day already looks pretty full. Should we move things around?")
    ]
    @State private var player: AVPlayer? = nil
    @State private var inputText = ""
    @State private var scrollToBottomID = UUID()
    
    var cardBackground: Color {
        #if os(iOS)
        return Color(UIColor.systemGray6)
        #else
        return Color.gray.opacity(0.15)
        #endif
    }

    var inputBackground: Color {
        #if os(iOS)
        return Color(UIColor.systemGray5)
        #else
        return Color.gray.opacity(0.2)
        #endif
    }

    var body: some View {
        VStack(spacing: 0) {
            // Agent Card
            HStack(spacing: 12) {
                Image(agent.imageName)
                    .resizable()
                    .aspectRatio(contentMode: .fill)
                    .frame(width: 50, height: 50)
                    .clipShape(Circle())

                VStack(alignment: .leading, spacing: 4) {
                    Text(agent.name)
                        .font(.title3)
                        .fontWeight(.semibold)
                    Text(agent.title)
                        .font(.caption)
                        .foregroundColor(.gray)
                }

                Spacer()

                Button(action: {
                    agent.isSpeaking.toggle()
                    print("🔊 Toggled speaker. isSpeaking is now: \(agent.isSpeaking)")
                }) {
                    Image(systemName: agent.isSpeaking ? "speaker.wave.2.fill" : "speaker.slash.fill")
                        .foregroundColor(agent.isSpeaking ? .blue : .gray)
                }
            }
            .padding()
            .background(cardBackground)
            .cornerRadius(24)
            .shadow(color: .black.opacity(0.05), radius: 6, x: 0, y: 2)
            .padding(.horizontal)

            // Messages
            ScrollViewReader { scrollViewProxy in
                ScrollView {
                    VStack(spacing: 12) {
                        ForEach(messages) { message in
                            ChatBubbleView(message: message)
                        }
                        // Invisible spacer to scroll to
                        Color.clear
                            .frame(height: 1)
                            .id(scrollToBottomID)
                    }
                    .padding(.top)
                    .frame(maxWidth: .infinity, alignment: .top)
                }
                .onChange(of: messages.count) {
                    withAnimation {
                        scrollViewProxy.scrollTo(scrollToBottomID, anchor: .bottom)
                    }
                }
            }

            // Input Field
            HStack {
                TextField("Message...", text: $inputText)
                    .padding(12)
                    .background(inputBackground)
                    .cornerRadius(20)

                Button(action: {
                    guard !inputText.isEmpty else { return }

                    let userMessage = ChatMessage(isFromUser: true, text: inputText)
                    messages.append(userMessage)
                    let outgoingText = inputText
                    inputText = ""

                    ChatService.shared.sendMessage(to: agent.name.lowercased(), input: outgoingText, voiceID: agent.voiceID) { result in
                        switch result {
                        case .success(let response):
                            print("🟢 GPT-4 response:", response.text)
                            print("🟢 Audio URL:", "https://nooro-backend.onrender.com\(response.audio_url)")
                            let reply = ChatMessage(isFromUser: false, text: response.text)
                            DispatchQueue.main.async {
                                messages.append(reply)
                                if agent.isSpeaking {
                                    playAudio(from: "https://nooro-backend.onrender.com\(response.audio_url)")
                                }
                            }
                        case .failure(let error):
                            print("❌ Chat API error: \(error.localizedDescription)")
                        }
                    }
                }) {
                    Image(systemName: "paperplane.fill")
                        .padding(.horizontal)
                        .foregroundColor(.blue)
                }
            }
            .padding(.horizontal)
            .padding(.bottom, 10)
        }
    }

    // MARK: - Audio Playback
   
    func playAudio(from urlString: String) {
        guard let url = URL(string: urlString) else { return }
        player = AVPlayer(url: url)
        player?.play()
    }
}
