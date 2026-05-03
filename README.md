# Blazing Tails — AI Character Pipeline

**Repo:** Kaoz625/blazing-tails-characters (create manually on GitHub)
**Purpose:** Generate 84 unique AI model personas per month across 12 AI models × 7 user groups = 1,008 characters/year

## Structure

- 12 AI model personas (one character per model per month)
- 7 user group categories (character tuned to specific user type)
- Each character: name, personality, traits, backstory, user type match, visual description
- Output: JSON per character

## The 12 AI Model Personas

| # | Model | Persona Type |
|---|-------|-------------|
| 1 | Claude Opus | The Philosopher — deep thinker, measured, ethical |
| 2 | Claude Sonnet | The Strategist — balanced, analytical, action-oriented |
| 3 | Claude Haiku | The Swift — fast, concise, minimalist |
| 4 | GPT-4o | The Generalist — adaptable, knowledgeable, friendly |
| 5 | GPT-4o Mini | The Helper — efficient, accessible, practical |
| 6 | Gemini Pro | The Researcher — data-driven, thorough, visual |
| 7 | Gemini Flash | The Sprinter — rapid, energetic, task-focused |
| 8 | Llama 3 | The Free Spirit — open, unconstrained, community-rooted |
| 9 | Mistral | The European — refined, precise, multilingual |
| 10 | Grok | The Rebel — edgy, humorous, anti-establishment |
| 11 | Perplexity | The Seeker — curious, search-first, citation-obsessed |
| 12 | Command R+ | The Enterprise — formal, structured, business-ready |

## The 7 User Groups

| # | Group | Description |
|---|-------|-------------|
| 1 | Creators | Artists, musicians, YouTubers, writers |
| 2 | Hustlers | Entrepreneurs, side-hustlers, business owners |
| 3 | Students | High school, college, lifelong learners |
| 4 | Professionals | Corporate, career-focused, 9-to-5 |
| 5 | Gamers | Competitive, casual, streaming community |
| 6 | Explorers | Travelers, adventure seekers, curious minds |
| 7 | Nurturers | Parents, caregivers, community leaders |

## Monthly Cycle

Month 1: 12 models × 7 groups = 84 characters (cycle 001)
Month 12: Same models/groups, evolved personalities (cycle 012)
Year 1 total: 1,008 unique characters

## Usage

```bash
python generate_characters.py --model "Claude Opus" --group "Creators" --cycle 1
```

Output: `characters/cycle-001/claude-opus-creators.json`
