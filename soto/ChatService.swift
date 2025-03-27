//
//  ChatService.swift
//  soto
//
//  Created by Joshua Soto on 3/27/25.
//
import Foundation

struct ChatResponse: Codable {
    let text: String
    let audio_url: String
}

class ChatService {
    static let shared = ChatService()

    func sendMessage(to agent: String, input: String, voiceID: String, completion: @escaping (Result<ChatResponse, Error>) -> Void) {
        guard let url = URL(string: "https://nooro-backend.onrender.com/chat") else { return }

        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")

        let payload = [
            "agent": agent,
            "input": input,
            "voice_id": voiceID
        ]

        do {
            request.httpBody = try JSONEncoder().encode(payload)
        } catch {
            completion(.failure(error))
            return
        }

        URLSession.shared.dataTask(with: request) { data, _, error in
            if let error = error {
                completion(.failure(error))
                return
            }

            guard let data = data else { return }

            do {
                let decoded = try JSONDecoder().decode(ChatResponse.self, from: data)
                completion(.success(decoded))
            } catch {
                completion(.failure(error))
            }
        }.resume()
    }
}
