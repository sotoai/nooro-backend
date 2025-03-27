//
//  ChatBubbleView.swift
//  soto
//
//  Created by Joshua Soto on 3/27/25.
//

import SwiftUI

struct ChatBubbleView: View {
    let message: ChatMessage

    var body: some View {
        HStack {
            if message.isFromUser { Spacer() }

            Text(message.text)
                .padding(12)
                .background(
                    RoundedRectangle(cornerRadius: 18)
                        .stroke(Color.gray.opacity(0.4), lineWidth: 1)
                        .background(Color.white.cornerRadius(18))
                )
                .foregroundColor(.black)
                .multilineTextAlignment(.leading)
                .fixedSize(horizontal: false, vertical: true)
                .frame(maxWidth: 280, alignment: message.isFromUser ? .trailing : .leading)

            if !message.isFromUser { Spacer() }
        }
        .padding(.horizontal)
    }
}
