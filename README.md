# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

In this project I built a small music recommender system that suggests songs based on a user’s taste profile. My system compares song features like genre, mood, energy, and how acoustic a song is to what the user prefers. Then it gives each song a score and ranks them from best match to worst match.

The goal was basically to simulate how real apps recommend music, but in a simpler way. I also tested how changing the scoring logic affects the results and reflected on how this connects to real AI systems like Spotify.

---

## How The System Works

My system uses a content-based recommendation approach. That means it doesn’t look at other users, it only compares the features of each song to the user’s preferences.

Each `Song` includes:
- genre  
- mood  
- energy (how intense the song is)  
- tempo  
- acousticness (acoustic vs electronic)  

The `UserProfile` stores:
- favorite genre  
- favorite mood  
- target energy  
- whether the user prefers acoustic music or not  

To compute the score:
- The system gives **+2 points** if the genre matches  
- **+1.5 points** if the mood matches  
- It gives points based on how close the energy is to the user’s target  
- It also adds points depending on whether the song matches the user’s acoustic preference  

After scoring every song, the system sorts them from highest score to lowest and returns the top 5 songs.

So basically:
User preferences → compare to every song → calculate score → rank → return best matches


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

I ran an experiment where I changed the scoring weights. I reduced how important genre was and increased how important energy was.

After doing that, songs that had similar energy to the user started ranking higher even if they weren’t the same genre. This made the recommendations feel more flexible, but also sometimes less accurate because genre didn’t matter as much anymore.

I also tested different user profiles like:

high-energy pop
chill lofi
intense rock


---

## Limitations and Risks

this system has a lot of limitations because it’s very simple.

It only uses a small dataset (10 songs), so recommendations are limited
It doesn’t understand lyrics, language, or meaning
It simplifies music taste into just a few features
It can easily over-favor one genre or type of song depending on the weights

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

