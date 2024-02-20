//
//  BeaconApp.swift
//  Beacon
//
//  Created by Aniket Mishra on 2024-02-19.
//

import SwiftUI

@main
struct BeaconApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }.windowStyle(.volumetric)

        ImmersiveSpace(id: "ImmersiveSpace") {
            ImmersiveView()
        }.immersionStyle(selection: .constant(.progressive), in: .progressive)
    }
}
