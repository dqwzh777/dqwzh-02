#!/usr/bin/env swift

import AppKit
import Foundation
import Vision

guard CommandLine.arguments.count == 2 else {
    FileHandle.standardError.write(Data("usage: vision_ocr.swift IMAGE\n".utf8))
    exit(2)
}

let imageURL = URL(fileURLWithPath: CommandLine.arguments[1])
guard let image = NSImage(contentsOf: imageURL) else {
    FileHandle.standardError.write(Data("cannot open image\n".utf8))
    exit(3)
}

var proposed = NSRect(origin: .zero, size: image.size)
guard let cgImage = image.cgImage(forProposedRect: &proposed, context: nil, hints: nil) else {
    FileHandle.standardError.write(Data("cannot convert image\n".utf8))
    exit(4)
}

var observations: [VNRecognizedTextObservation] = []
var recognitionError: Error?
let request = VNRecognizeTextRequest { request, error in
    recognitionError = error
    observations = request.results as? [VNRecognizedTextObservation] ?? []
}
request.recognitionLevel = .accurate
request.usesLanguageCorrection = true
request.recognitionLanguages = ["zh-Hans", "en-US"]

do {
    try VNImageRequestHandler(cgImage: cgImage, options: [:]).perform([request])
} catch {
    recognitionError = error
}

if let error = recognitionError {
    FileHandle.standardError.write(Data("OCR failed: \(error.localizedDescription)\n".utf8))
    exit(5)
}

let sorted = observations.sorted { lhs, rhs in
    let delta = lhs.boundingBox.midY - rhs.boundingBox.midY
    if abs(delta) > 0.015 { return delta > 0 }
    return lhs.boundingBox.minX < rhs.boundingBox.minX
}

let lines = sorted.compactMap { $0.topCandidates(1).first?.string }
print(lines.joined(separator: "\n"))
