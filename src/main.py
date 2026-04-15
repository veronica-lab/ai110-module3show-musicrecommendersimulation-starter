from src.recommender import load_songs, recommend_songs


def print_profile_results(profile_name, user_prefs, songs):
    print("\n" + "=" * 60)
    print(profile_name)
    print("=" * 60)

    recommendations = recommend_songs(user_prefs, songs, k=5)

    for song, score, explanation in recommendations:
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    pop_profile = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "likes_acoustic": False
    }

    lofi_profile = {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.4,
        "likes_acoustic": True
    }

    rock_profile = {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.9,
        "likes_acoustic": False
    }

    print_profile_results("High-Energy Pop Profile", pop_profile, songs)
    print_profile_results("Chill Lofi Profile", lofi_profile, songs)
    print_profile_results("Deep Intense Rock Profile", rock_profile, songs)


if __name__ == "__main__":
    main()
    