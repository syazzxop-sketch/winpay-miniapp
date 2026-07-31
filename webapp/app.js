function submitCode(){

let code=document.getElementById("invite").value.trim();

if(code==""){
alert("Please enter Invitation Code");
return;
}

document.querySelector(".card").innerHTML=`

<h2>🎉 Safal!!</h2>

<p>

✅ System ne aapki jankari
successfully save kar li hai.

</p>

<div class="menu">

<div class="box">💰<br>Deposit (UPI)</div>

<div class="box">🎁<br>Bonus Offers</div>

<div class="box">📖<br>How To Deposit</div>

<div class="box">💎<br>Premium</div>

<div class="box full">🎧 Customer Support</div>

<div class="box full">✅ Post & Share ₹17-177<br><small>Coming Soon</small></div>

</div>

`;

}