#!/usr/bin/env python3
"""
Blazing Tails AI Character Pipeline
Generates unique character profiles: 12 AI models x 7 user groups x monthly cycle
"""
import json
import argparse
import os
import random
from datetime import datetime

AI_MODELS = {
    "Claude Opus": {
        "archetype": "The Philosopher",
        "base_traits": ["contemplative", "ethical", "eloquent", "measured", "wise"],
        "communication_style": "thoughtful and nuanced",
        "signature_phrase": "Let us consider the deeper implications...",
    },
    "Claude Sonnet": {
        "archetype": "The Strategist",
        "base_traits": ["analytical", "balanced", "decisive", "creative", "thorough"],
        "communication_style": "clear and structured",
        "signature_phrase": "Here is the most effective path forward...",
    },
    "Claude Haiku": {
        "archetype": "The Swift",
        "base_traits": ["concise", "precise", "minimalist", "efficient", "sharp"],
        "communication_style": "brief and impactful",
        "signature_phrase": "Quick answer:",
    },
    "GPT-4o": {
        "archetype": "The Generalist",
        "base_traits": ["adaptable", "knowledgeable", "friendly", "versatile", "helpful"],
        "communication_style": "warm and conversational",
        "signature_phrase": "Great question! Here is what I know...",
    },
    "GPT-4o Mini": {
        "archetype": "The Helper",
        "base_traits": ["efficient", "accessible", "practical", "reliable", "responsive"],
        "communication_style": "direct and accessible",
        "signature_phrase": "I can help with that right away.",
    },
    "Gemini Pro": {
        "archetype": "The Researcher",
        "base_traits": ["data-driven", "thorough", "visual", "systematic", "curious"],
        "communication_style": "detailed and evidence-based",
        "signature_phrase": "According to the latest information...",
    },
    "Gemini Flash": {
        "archetype": "The Sprinter",
        "base_traits": ["rapid", "energetic", "task-focused", "agile", "dynamic"],
        "communication_style": "fast and punchy",
        "signature_phrase": "On it! Here is the fast version:",
    },
    "Llama 3": {
        "archetype": "The Free Spirit",
        "base_traits": ["open", "unconstrained", "community-rooted", "raw", "authentic"],
        "communication_style": "casual and unfiltered",
        "signature_phrase": "Real talk —",
    },
    "Mistral": {
        "archetype": "The European",
        "base_traits": ["refined", "precise", "multilingual", "cultured", "methodical"],
        "communication_style": "formal and precise",
        "signature_phrase": "Allow me to address this systematically.",
    },
    "Grok": {
        "archetype": "The Rebel",
        "base_traits": ["edgy", "humorous", "anti-establishment", "bold", "irreverent"],
        "communication_style": "sarcastic and direct",
        "signature_phrase": "Hot take incoming:",
    },
    "Perplexity": {
        "archetype": "The Seeker",
        "base_traits": ["curious", "search-first", "citation-obsessed", "inquisitive", "thorough"],
        "communication_style": "research-oriented with sources",
        "signature_phrase": "Based on multiple sources...",
    },
    "Command R+": {
        "archetype": "The Enterprise",
        "base_traits": ["formal", "structured", "business-ready", "professional", "reliable"],
        "communication_style": "corporate and structured",
        "signature_phrase": "Per your request, here is the formal response:",
    },
}

USER_GROUPS = {
    "Creators": {
        "profile": "Artists, musicians, YouTubers, writers",
        "values": ["expression", "originality", "audience", "craft", "vision"],
        "pain_points": ["creative block", "monetization", "algorithm changes", "burnout"],
        "language": ["collab", "drop", "vibe", "authentic", "creative flow"],
    },
    "Hustlers": {
        "profile": "Entrepreneurs, side-hustlers, small business owners",
        "values": ["growth", "revenue", "efficiency", "independence", "results"],
        "pain_points": ["cash flow", "scaling", "competition", "time management"],
        "language": ["ROI", "grind", "stack", "pivot", "build"],
    },
    "Students": {
        "profile": "High school, college, lifelong learners",
        "values": ["knowledge", "achievement", "growth", "belonging", "future"],
        "pain_points": ["deadlines", "debt", "focus", "career uncertainty"],
        "language": ["study", "grades", "campus", "major", "internship"],
    },
    "Professionals": {
        "profile": "Corporate workers, career-focused individuals",
        "values": ["advancement", "stability", "expertise", "network", "impact"],
        "pain_points": ["work-life balance", "recognition", "office politics", "burnout"],
        "language": ["KPIs", "deliverables", "stakeholders", "bandwidth", "alignment"],
    },
    "Gamers": {
        "profile": "Competitive, casual, and streaming community",
        "values": ["skill", "community", "entertainment", "competition", "content"],
        "pain_points": ["toxicity", "lag", "monetization", "burnout", "hardware costs"],
        "language": ["GG", "meta", "grind", "stream", "clip"],
    },
    "Explorers": {
        "profile": "Travelers, adventure seekers, curious minds",
        "values": ["experience", "freedom", "discovery", "stories", "growth"],
        "pain_points": ["budget", "planning complexity", "FOMO", "safety"],
        "language": ["itinerary", "off the beaten path", "local gems", "backpack", "wanderlust"],
    },
    "Nurturers": {
        "profile": "Parents, caregivers, community leaders",
        "values": ["wellbeing", "connection", "safety", "legacy", "support"],
        "pain_points": ["time scarcity", "cost of living", "balance", "isolation"],
        "language": ["community", "family", "support", "resources", "together"],
    },
}

NYC_NAMES_FIRST = ["Jordan", "Alex", "Sage", "River", "Phoenix", "Sky", "Zion", "Nova", "Blaze", "Storm",
                    "Ash", "Ember", "Onyx", "Cleo", "Kai", "Remi", "Demi", "Lux", "Raven", "Cruz"]
NYC_NAMES_LAST = ["Rivera", "Okonkwo", "Chen", "Williams", "Martinez", "Thompson", "Patel", "Johnson",
                   "Garcia", "Kim", "Torres", "Jackson", "Nguyen", "Brown", "Davis", "Robinson", "Lewis", "Walker"]

BOROUGHS = ["Brooklyn", "Queens", "The Bronx", "Harlem", "Lower East Side", "Bed-Stuy", "Crown Heights",
             "Astoria", "Flushing", "Jamaica", "Riverdale", "Bushwick", "Williamsburg"]


def generate_character(model_name: str, group_name: str, cycle: int) -> dict:
    model = AI_MODELS[model_name]
    group = USER_GROUPS[group_name]

    random.seed(f"{model_name}-{group_name}-cycle{cycle:03d}")

    first = random.choice(NYC_NAMES_FIRST)
    last = random.choice(NYC_NAMES_LAST)
    borough = random.choice(BOROUGHS)
    age = random.randint(18, 42)

    # Blend model traits with group values
    personality_traits = model["base_traits"][:3] + random.sample(group["values"], 2)
    backstory_pain = random.choice(group["pain_points"])
    group_word = random.choice(group["language"])

    backstory = (
        f"{first} {last} is a {age}-year-old {group['profile'].split(',')[0].lower()} "
        f"from {borough}, NYC. "
        f"They connect with the {model['archetype']} energy because they need {backstory_pain} "
        f"solved — fast, clearly, and without the noise. "
        f"They use the word '{group_word}' in almost every conversation. "
        f"Cycle {cycle:03d} evolution: more confident, harder questions."
    )

    return {
        "id": f"{model_name.lower().replace(' ', '-')}-{group_name.lower()}-cycle{cycle:03d}",
        "cycle": cycle,
        "generated_at": datetime.now().isoformat(),
        "model": model_name,
        "user_group": group_name,
        "name": f"{first} {last}",
        "age": age,
        "location": f"{borough}, NYC",
        "archetype": model["archetype"],
        "personality_traits": personality_traits,
        "communication_style": model["communication_style"],
        "signature_phrase": model["signature_phrase"],
        "user_profile": group["profile"],
        "core_values": group["values"][:3],
        "primary_pain_point": backstory_pain,
        "group_language": group["language"][:3],
        "backstory": backstory,
        "visual_description": (
            f"Profile image: {age}-year-old from {borough}. "
            f"Style reflects {group_name.lower()} culture with {model['archetype'].lower()} energy. "
            f"NYC street aesthetic."
        ),
    }


def generate_full_cycle(cycle: int, output_dir: str = "characters") -> list:
    cycle_dir = os.path.join(output_dir, f"cycle-{cycle:03d}")
    os.makedirs(cycle_dir, exist_ok=True)

    all_characters = []
    for model_name in AI_MODELS:
        for group_name in USER_GROUPS:
            char = generate_character(model_name, group_name, cycle)
            all_characters.append(char)
            filename = f"{model_name.lower().replace(' ', '-')}-{group_name.lower()}.json"
            filepath = os.path.join(cycle_dir, filename)
            with open(filepath, "w") as f:
                json.dump(char, f, indent=2)

    # Write cycle index
    index_path = os.path.join(cycle_dir, "_index.json")
    with open(index_path, "w") as f:
        json.dump({"cycle": cycle, "total": len(all_characters),
                   "characters": [c["id"] for c in all_characters]}, f, indent=2)

    print(f"Generated {len(all_characters)} characters for cycle {cycle:03d} → {cycle_dir}/")
    return all_characters


def main():
    parser = argparse.ArgumentParser(description="Blazing Tails AI Character Generator")
    parser.add_argument("--model", help="AI model name (or 'all')")
    parser.add_argument("--group", help="User group (or 'all')")
    parser.add_argument("--cycle", type=int, default=1, help="Monthly cycle number (1-12)")
    parser.add_argument("--all-cycles", type=int, help="Generate N full monthly cycles")
    parser.add_argument("--output", default="characters", help="Output directory")
    args = parser.parse_args()

    if args.all_cycles:
        for c in range(1, args.all_cycles + 1):
            generate_full_cycle(c, args.output)
        print(f"Done. Generated {args.all_cycles * 84} total characters.")
        return

    if args.model == "all" or args.group == "all" or (not args.model and not args.group):
        generate_full_cycle(args.cycle, args.output)
        return

    model = args.model or list(AI_MODELS.keys())[0]
    group = args.group or list(USER_GROUPS.keys())[0]

    if model not in AI_MODELS:
        print(f"Unknown model. Choose from: {', '.join(AI_MODELS.keys())}")
        return
    if group not in USER_GROUPS:
        print(f"Unknown group. Choose from: {', '.join(USER_GROUPS.keys())}")
        return

    char = generate_character(model, group, args.cycle)
    print(json.dumps(char, indent=2))


if __name__ == "__main__":
    main()
