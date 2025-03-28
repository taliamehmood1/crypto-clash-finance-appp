import streamlit as st
import random
import time
import pandas as pd

st.markdown(
    "<h1 style='text-align: center; color: #FF5733;'>🚀 Crypto Clash – The Ultimate Finance Battle! ⚔️</h1>", 
    unsafe_allow_html=True
)


# 🎈 Balloons Effect only on Home Page
def show_balloons():
    st.session_state.show_balloons = True

if "show_balloons" not in st.session_state:
    show_balloons()



st.write("Dive into the world of finance like never before! This interactive finance app lets you explore, play, and learn through exciting financial activities! 💰Sharpen your skills, make smart financial decisions, and have a blast along the way! 🎯🔥")

# 🎭 Activity Selection
activity = st.selectbox("🎮 Choose Your Activity:", 
                        ["Select an Activity", "1v1 Finance Quiz Battle", "Crypto Market Prediction Game", "Risky Investment Challenge", "AI Financial Advisor"])

# 🎈 Show balloons only when home page is opened
if st.session_state.show_balloons:
    st.balloons()
    st.session_state.show_balloons = False  # Disable after first display

# 🎯 1v1 Finance Quiz Battle
if activity == "1v1 Finance Quiz Battle":
    st.header("🧠 1v1 Finance Quiz Battle!")

    questions = [
        {"question": "What does ROI stand for?", "options": ["Return on Investment", "Rate of Interest", "Revenue of Industry"], "answer": "Return on Investment"},
        {"question": "Which asset is the most liquid?", "options": ["Real Estate", "Stocks", "Cash"], "answer": "Cash"},
        {"question": "What does ETF stand for?", "options": ["Electronic Transfer Fund", "Exchange-Traded Fund", "Equity Trade Finance"], "answer": "Exchange-Traded Fund"},
    ]

    score = 0
    for q in questions:
        answer = st.radio(f"❓ {q['question']}", q["options"], index=None)
        if answer and answer == q["answer"]:
            score += 1

    if st.button("Submit Answers"):
        if score == len(questions):
            st.success("🎉 Perfect Score! You're a finance genius!")
            st.snow()  # 🎊 Celebration effect on perfect score
        else:
            st.warning(f"You scored {score}/{len(questions)}. Keep Learning! 🔥")

# 📈 Crypto Market Prediction Game
elif activity == "Crypto Market Prediction Game":
    st.header("📊 Predict the Crypto Market!")

    # Fake Crypto Price Movement Graph
    price_trend = [random.randint(90, 110) for _ in range(10)]
    st.line_chart(price_trend)

    user_choice = st.radio("📉 Will the price go UP or DOWN?", ["UP", "DOWN"], index=None)
    
    if st.button("Submit Prediction"):
        actual_movement = "UP" if price_trend[-1] > price_trend[0] else "DOWN"
        if user_choice == actual_movement:
            st.success("✅ Correct Prediction! 🚀")  
        else:
            st.warning("❌ Incorrect! Try Again.")  # ❌ Now only shows for wrong answers, nothing extra.

# 🎰 Risky Investment Challenge (New Game)
elif activity == "Risky Investment Challenge":
    st.header("🎰 Risky Investment Challenge! 💸")

    if "investment_balance" not in st.session_state:
        st.session_state.investment_balance = 10000  # Start with $10,000

    assets = ["Bitcoin", "Ethereum", "NFTs", "Tech Stocks", "Penny Stocks"]
    chosen_asset = st.selectbox("📈 Choose an Asset to Invest In:", assets)

    investment_amount = st.slider("💰 How much do you want to invest?", min_value=100, max_value=st.session_state.investment_balance, step=100)

    if st.button("📊 Invest Now!"):
        st.write(f"⏳ Investing in {chosen_asset}...")
        with st.spinner("Market Fluctuating... 📉📈"):
            time.sleep(3)  # Simulate market movement

        # 50-50 chance of doubling or halving the investment
        if random.choice([True, False]):
            st.session_state.investment_balance += investment_amount  # Double money
            st.success(f"🚀 Wow! Your {chosen_asset} investment doubled! New Balance: ${st.session_state.investment_balance}")
        else:
            st.session_state.investment_balance -= investment_amount // 2  # Lose half
            st.error(f"📉 Oops! Your {chosen_asset} investment crashed. New Balance: ${st.session_state.investment_balance}")

    st.write(f"🏦 Current Balance: **${st.session_state.investment_balance}**")

# 🤖 AI Financial Advisor
elif activity == "AI Financial Advisor":
    st.header("🤖 AI Financial Advisor")

    uploaded_file = st.file_uploader("📂 Upload your financial data (CSV)", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("📊 Your uploaded data:")
        st.dataframe(df)

        # ✅ Fix: Case-insensitive column matching
        df.columns = df.columns.str.lower()  # Convert column names to lowercase
        if "income" in df.columns and ("expense" in df.columns or "expenses" in df.columns):
            total_income = df["income"].sum()
            total_expense = df["expense"].sum() if "expense" in df.columns else df["expenses"].sum()
            savings = total_income - total_expense

            st.write(f"💰 Total Income: ${total_income}")
            st.write(f"💸 Total Expenses: ${total_expense}")
            st.write(f"💾 Savings: ${savings}")

            if savings > 0:
                st.success("✅ You're saving money! Keep up the good financial habits! 🚀")
            else:
                st.warning("⚠️ You're spending more than you earn! Try to reduce unnecessary expenses. 📉")
        else:
            st.error("❌ Error: Make sure your file has 'Income' and 'Expense' (or 'Expenses') columns.")
