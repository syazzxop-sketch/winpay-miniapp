const invitePage = document.getElementById("invitePage");
const homePage = document.getElementById("homePage");

const inviteBtn = document.getElementById("inviteBtn");
const inviteInput = document.getElementById("inviteCode");

inviteBtn.onclick = function () {

    if (inviteInput.value.trim() === "") {
        alert("Please enter Invitation Code");
        return;
    }

    invitePage.style.display = "none";
    homePage.style.display = "block";
};

function openDeposit() {
    alert(
`💰 OFFLINE DEPOSIT

━━━━━━━━━━━━━━

UPI ID:
winpay@upi

✅ Send payment screenshot
to Customer Support.

━━━━━━━━━━━━━━`
    );
}

function openBonus() {
    alert(
`🎁 BONUS OFFERS

━━━━━━━━━━━━━━

₹500   ➜ ₹625
₹1000  ➜ ₹1356
₹1500  ➜ ₹1751
₹2000  ➜ ₹2411
₹2500  ➜ ₹2806
₹3000  ➜ ₹3454
₹3500  ➜ ₹4009
₹4000  ➜ ₹4563
₹4500  ➜ ₹4987
₹5000  ➜ ₹5521

━━━━━━━━━━━━━━

🔥 Bonus after successful deposit`
    );
}

function openHow() {
    alert(
`📖 HOW TO DEPOSIT

━━━━━━━━━━━━━━

① Click Deposit

② Select Amount

③ Pay using UPI

④ Send Screenshot

⑤ Balance Added after Verification ✅`
    );
}

function openShare() {
    alert(
`🎁 POST & SHARE

━━━━━━━━━━━━━━

🚧 Coming Soon...

Reward ₹17 - ₹177`
    );
}

function openSupport() {
    window.open("https://t.me/YOUR_USERNAME");
}