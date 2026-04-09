from flask import Flask, render_template_string, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "ssm_bet_security_2025" # Kan ayaa ah furaha is-maamulka system-ka

# 1. DESIGN-KA IYO LOGIC-KA ISKU DHAFFAN
SSM_MASTER_UI = """
<!DOCTYPE html>
<html lang="so">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SSMBet - Official App</title>
    <script src="https://tailwindcss.com"></script>
    <style>
        body { background-color: #f1f4f7; font-family: 'Segoe UI', sans-serif; }
        .neon-green { background-color: #39FF14; }
        .modal { transition: transform 0.4s ease; transform: translateY(100%); z-index: 100; position: fixed; inset: 0; background: white; }
        .modal.open { transform: translateY(0); }
    </style>
</head>
<body class="pb-24">

    <!-- HEADER -->
    <header class="bg-white p-3 flex justify-between items-center border-b">
        <div class="text-2xl font-black text-green-600 italic tracking-tighter">SSMBET</div>
        <div class="flex items-center space-x-3">
            {% if session.get('user_id') %}
                <div class="bg-gray-100 px-3 py-1 rounded-full text-[10px] font-bold">ID: {{ session['user_id'] }} | ${{ session['balance'] }}</div>
            {% else %}
                <button onclick="openModal('reg-modal')" class="bg-green-500 text-white px-4 py-1 rounded-full text-xs font-bold">Register</button>
            {% endif %}
        </div>
    </header>

    <!-- CONTENT -->
    <main class="p-4">
        <!-- Banner -->
        <div class="bg-gray-900 rounded-2xl p-5 text-white h-36 flex flex-col justify-between border-l-4 border-green-500 shadow-xl mb-6">
            <h4 class="font-black text-lg italic">200% BONUS ON DEPOSIT</h4>
            <button onclick="checkAccess('/deposit')" class="bg-green-500 text-black text-[10px] font-bold px-4 py-1.5 rounded-full w-fit uppercase">Deposit Now</button>
        </div>

        <h3 class="font-bold text-sm mb-3">🔥 LIVE Matches</h3>
        <div class="bg-white rounded-2xl p-4 shadow-sm border border-gray-50">
            <div class="flex justify-between items-center mb-6">
                <div class="text-center w-1/3 text-[11px] font-bold">Arsenal</div>
                <div class="text-2xl font-black italic">1 : 0</div>
                <div class="text-center w-1/3 text-[11px] font-bold">Chelsea</div>
            </div>
            <div class="grid grid-cols-3 gap-2">
                <button onclick="checkAccess('/slip')" class="bg-gray-50 p-2 rounded-lg text-xs font-bold border">1.95</button>
                <button onclick="checkAccess('/slip')" class="bg-gray-50 p-2 rounded-lg text-xs font-bold border">3.40</button>
                <button onclick="checkAccess('/slip')" class="bg-gray-50 p-2 rounded-lg text-xs font-bold border">4.10</button>
            </div>
        </div>
    </main>

    <!-- REGISTRATION MODAL -->
    <div id="reg-modal" class="modal flex flex-col">
        <div class="p-4 flex items-center border-b">
            <button onclick="closeModal('reg-modal')" class="text-3xl mr-4 text-gray-300">&times;</button>
            <h2 class="text-lg font-black uppercase">Registration</h2>
        </div>
        <form action="/register" method="POST" class="p-6 space-y-4">
            <input type="text" name="username" placeholder="Username" class="w-full p-4 bg-gray-100 rounded-xl font-bold text-sm outline-none" required>
            <input type="text" name="phone" placeholder="Mobcash Phone (25261...)" class="w-full p-4 bg-gray-100 rounded-xl font-bold text-sm outline-none" required>
            <button type="submit" class="w-full py-4 neon-green text-black font-black rounded-xl shadow-lg uppercase tracking-widest text-xs">Confirm & Get ID</button>
        </form>
    </div>

    <!-- BOTTOM NAV -->
    <nav class="fixed bottom-0 left-0 right-0 bg-white border-t p-2 flex justify-around items-center text-[10px] font-bold text-gray-400 z-50">
        <div class="text-center text-green-500 cursor-pointer" onclick="location.href='/'">🏠<br>Home</div>
        <div class="text-center cursor-pointer" onclick="checkAccess('/slip')">📑<br>Slip</div>
        <div class="text-center cursor-pointer" onclick="checkAccess('/profile')">👤<br>Profile</div>
    </nav>

    <script>
        function openModal(id) { document.getElementById(id).classList.add('open'); }
        function closeModal(id) { document.getElementById(id).classList.remove('open'); }

        // IS-MAAMULKA SYSTEM-KA: Hubi haddii uu user-ku jiro
        function checkAccess(target) {
            const isLoggedIn = {{ 'true' if session.get('user_id') else 'false' }};
            if (!isLoggedIn) {
                alert("Neeo! Waa inaad is-diiwaangelisaa marka hore si aad u hesho xuquuqda website-ka.");
                openModal('reg-modal');
            } else {
                window.location.href = target;
            }
        }
    </script>
</body>
</html>
"""

# 2. BACKEND ACTIONS
@app.route('/')
def index():
    return render_template_string(SSM_MASTER_UI)

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    phone = request.form.get('phone')
    if username and phone:
        # System-ka ayaa iskiis u abuuraya xogta macmiilka
        session['user_id'] = random.randint(100000, 999999)
        session['username'] = username
        session['balance'] = 100.0  # Hadiyad bilaash ah
        return redirect(url_for('index'))
    return "Fadlan buuxi dhammaan meelaha maran!"

@app.route('/deposit')
def deposit():
    if 'user_id' not in session: return redirect(url_for('index'))
    return "<h1>Bogga Deposit-ka (Mobcash) waa kani!</h1>"

@app.route('/profile')
def profile():
    if 'user_id' not in session: return redirect(url_for('index'))
    return f"<h1>Ku soo dhowow {session['username']}! ID-gaagu waa {session['user_id']}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
