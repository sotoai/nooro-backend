import SwiftUI

struct Agent {
    let id = UUID()
    let name: String
    let title: String
    let imageName: String
    var isSpeaking: Bool
}

struct AgentChatView: View {
    let agent: Agent
    @State private var messages: [ChatMessage] = [
        ChatMessage(isFromUser: true, text: "Hi Sam. Can you please schedule some time with Mike Haro this coming Wednesday?"),
        ChatMessage(isFromUser: false, text: "Absolutely! Your day already looks pretty full. Should we move things around?")
    ]
    @State private var inputText = ""

    // MARK: - Computed Colors (Platform-Safe)
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
                    // Handle speaker toggle
                }) {
                    Image(systemName: agent.isSpeaking ? "speaker.wave.2.fill" : "speaker.slash.fill")
                        .foregroundColor(.gray)
                }
            }
            .padding()
            .background(cardBackground)
            .cornerRadius(24)
            .shadow(color: .black.opacity(0.05), radius: 6, x: 0, y: 2)
            .padding(.horizontal)

            // Messages
            ScrollView {
                VStack(spacing: 12) {
                    ForEach(messages) { message in
                        ChatBubbleView(message: message)
                    }
                }
                .padding(.top)
                .frame(maxWidth: .infinity, alignment: .top) // <- add this
            }

            // Input Field
            HStack {
                TextField("Message...", text: $inputText)
                    .padding(12)
                    .background(inputBackground)
                    .cornerRadius(20)

                Button(action: {
                    guard !inputText.isEmpty else { return }
                    messages.append(ChatMessage(isFromUser: true, text: inputText))
                    inputText = ""
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
}
