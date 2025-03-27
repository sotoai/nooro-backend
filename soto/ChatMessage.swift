//
//  ChatMessage.swift
//  soto
//
//  Created by Joshua Soto on 3/27/25.
//

import Foundation

struct ChatMessage: Identifiable {
    let id = UUID()
    let isFromUser: Bool
    let text: String
}
