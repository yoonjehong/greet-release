# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `greet()` accepts a new `punctuation` argument (default `"!"`); before, the ending was always `!`.

### Fixed

- `greet()` and the command line greet `world` for a blank name; before, `''` printed `Hello, !`.

## [0.1.0] - 2026-11-09

### Added

- `greet()` and the command line print the greeting `Hello, <name>!`.
