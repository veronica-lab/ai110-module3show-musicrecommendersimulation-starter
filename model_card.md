# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeMatch 1.0  

---

## 2. Intended Use  

This recommender is designed to suggest songs from a small catalog based on a user’s preferences like genre, mood, and energy level. It assumes that a user’s music taste can be represented through a few features and that similar songs will match what they like.

This system is not for real users. It’s meant to show how recommendation systems work in a simplified way.

---

## 3. How the Model Works  

The model works by comparing each song’s features to a user profile and giving it a score.

Each song has features like genre, mood, energy, tempo, and how acoustic it is. The user profile includes a favorite genre, favorite mood, a target energy level, and whether they prefer acoustic music or not.

The system gives points if the genre matches and if the mood matches. Then it adds more points depending on how close the song’s energy is to the user’s target energy. It also adds points depending on whether the song matches the user’s acoustic preference.

After scoring every song, the system ranks them from highest to lowest score and returns the top results.

Compared to the starter version, I added more detailed scoring by including energy closeness and acoustic preference instead of just basic matching.

---

## 4. Data  

The dataset contains 10 songs from a CSV file. Each song includes features like genre, mood, energy, tempo, valence, danceability, and acousticness.

The dataset includes a mix of genres like pop, lofi, rock, ambient, jazz, and indie. It also includes different moods like happy, chill, intense, relaxed, and moody.

However, the dataset is very small and does not represent all types of music. It also doesn’t include things like lyrics, language, or cultural context, which are important parts of music taste.

---

## 5. Strengths  

The system works well when the user has clear preferences, like wanting high-energy pop or chill lofi music. In those cases, the top recommendations usually match the expected vibe.

The scoring system also captures patterns like energy similarity pretty well. For example, songs with similar energy levels consistently rank higher.

Another strength is that the recommendations are easy to explain, since the system shows the reasons behind each score.

---

## 6. Limitations and Bias  

One limitation is that the system only uses a few features, so it ignores many important aspects of music like lyrics or personal meaning.

It can also be biased depending on the dataset. For example, if there are more pop songs, the system might recommend pop more often.

The scoring can also overfocus on certain features. If genre is weighted too heavily, it might ignore songs that match the vibe but are in a different genre.

This could be unfair in a real system because it might limit what users are exposed to and create a kind of filter bubble.

---

## 7. Evaluation  

I tested the recommender using different user profiles like high-energy pop, chill lofi, and intense rock.

For each profile, I looked at whether the top songs matched the expected vibe. In most cases, the results made sense, especially when both genre and energy aligned.

One thing that surprised me is how sensitive the system is to weight changes. When I reduced genre importance and increased energy importance, the recommendations changed a lot.

I also ran the system multiple times to see if the same songs kept appearing, which helped me notice patterns in the scoring.

---

## 8. Future Work  

If I had more time, I would expand the dataset with more songs and more genres to make the recommendations more diverse.

I would also add more features like lyrical themes or tempo ranges to better capture music preferences.

Another improvement would be making the system balance diversity, so it doesn’t always recommend very similar songs.

---

## 9. Personal Reflection  

This project helped me understand that recommendation systems are not as complex as they seem at first. At the core, they are just comparing data and assigning scores.

What surprised me the most is that even a simple model like this can still feel accurate when it matches the right features.

It also made me realize how easy it is for bias to show up. Small decisions, like how much weight to give a feature, can completely change what users see.

Overall, this changed how I think about apps like Spotify. Now I see that what we get recommended is heavily shaped by the system design, not just our taste.