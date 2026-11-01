
from flask import Flask, render_template_string

app = Flask(__name__)

DISCORD = "https://discord.gg/enhAzedgp"

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#090b16">

<title>DOG CHAT | Comunidade</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    background: #090b16;
    color: white;
    font-family: Inter, sans-serif;
    overflow-x: hidden;
    cursor: none;
}

a {
    text-decoration: none;
}

/* FUNDOS ANIMADOS */

#spaceCanvas,
#rainCanvas {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
}

#spaceCanvas {
    z-index: 0;
}

#rainCanvas {
    z-index: 50;
}

/* CONTEÚDO */

nav,
main,
footer {
    position: relative;
    z-index: 2;
}

/* CURSOR DE PATA */

.paw-cursor {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 10001;
    pointer-events: none;
    font-size: 25px;
    transform: translate(-50%, -50%);
    filter: drop-shadow(0 0 8px #a78bfa);
}

/* NAVEGAÇÃO */

nav {
    height: 82px;
    padding: 0 8%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #ffffff12;
    background: #090b16;
    position: relative;
    z-index: 5;
}

.logo {
    font-size: 23px;
    font-weight: 900;
    color: white;
}

.logo span {
    color: #a78bfa;
}

.nav-btn {
    padding: 12px 20px;
    border: 1px solid #ffffff30;
    color: white;
    border-radius: 10px;
    font-size: 13px;
    transition: .3s;
}

.nav-btn:hover {
    background: #635bdb;
}

/* INÍCIO */

.hero {
    position: relative;
    min-height: 690px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 100px 20px 70px;
    overflow: hidden;
}

.glow {
    position: absolute;
    width: 450px;
    height: 450px;
    background: #7048ff;
    filter: blur(180px);
    opacity: .22;
    pointer-events: none;
}

.tag {
    border: 1px solid #8b5cf680;
    background: #8b5cf61a;
    padding: 11px 18px;
    border-radius: 50px;
    color: #c4b5fd;
    font-size: 10px;
    letter-spacing: 1.5px;
    margin-bottom: 30px;
    position: relative;
    z-index: 2;
}

h1 {
    font-size: clamp(43px, 8vw, 82px);
    line-height: 1.08;
    font-weight: 900;
    letter-spacing: -4px;
    position: relative;
    z-index: 2;
}

.gradient {
    background: linear-gradient(
        90deg, #818cf8, #c084fc, #818cf8
    );
    background-size: 200%;
    -webkit-background-clip: text;
    color: transparent;
    animation: shine 5s linear infinite;
}

.description {
    max-width: 530px;
    color: #a1a1b5;
    font-size: 15px;
    line-height: 1.8;
    margin: 24px auto 30px;
    position: relative;
    z-index: 2;
}

/* CHROME ORBIT - LOGO GRANDE */

.hero-orbit {
    position: relative;
    width: 280px;
    height: 280px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 28px;
    perspective: 900px;
    cursor: pointer;
    z-index: 2;
    transition: transform .4s ease;
}

.hero-orbit .dog {
    position: relative;
    z-index: 3;
    width: 190px;
    height: 190px;
    object-fit: contain;
    border-radius: 50%;
    border: 2px solid #c4b5fd;
    background: #121020;
    box-shadow: 0 0 35px #8b5cf655;
    animation: float 4s ease-in-out infinite;
}

.orbit-ring {
    position: absolute;
    inset: 15px;
    border: 3px solid transparent;
    border-radius: 50%;
    pointer-events: none;
    background:
        linear-gradient(#090b16, #090b16) padding-box,
        conic-gradient(
            #ffffff,
            #8b5cf6,
            #dbeafe,
            #475569,
            #c084fc,
            #ffffff
        ) border-box;
    filter: drop-shadow(0 0 8px #a78bfa);
}

.ring-one {
    animation: orbitOne 5s linear infinite;
}

.ring-two {
    inset: 25px;
    animation: orbitTwo 4s linear infinite;
}

.ring-three {
    inset: 5px;
    animation: orbitThree 6s linear infinite;
}

@keyframes orbitOne {
    from {
        transform: rotateX(65deg) rotateZ(0deg);
    }
    to {
        transform: rotateX(65deg) rotateZ(360deg);
    }
}

@keyframes orbitTwo {
    from {
        transform: rotateY(65deg) rotateZ(360deg);
    }
    to {
        transform: rotateY(65deg) rotateZ(0deg);
    }
}

@keyframes orbitThree {
    from {
        transform: rotateX(65deg) rotateY(40deg) rotateZ(0deg);
    }
    to {
        transform: rotateX(65deg) rotateY(40deg) rotateZ(360deg);
    }
}

.hero-orbit.halo-active {
    transform: scale(1.08);
}

.hero-orbit.halo-active .orbit-ring {
    animation-duration: 1s;
    filter:
        drop-shadow(0 0 12px #ffffff)
        drop-shadow(0 0 25px #a78bfa);
}

/* BOTÃO DISCORD */

.join {
    display: inline-flex;
    gap: 12px;
    align-items: center;
    justify-content: center;
    padding: 19px 27px;
    background: linear-gradient(110deg, #635bdb, #9333ea);
    border-radius: 12px;
    color: white;
    font-size: 13px;
    font-weight: 800;
    box-shadow: 0 10px 40px #7048ff55;
    transition: .3s;
    position: relative;
    z-index: 2;
}

.join:hover {
    transform: translateY(-5px) scale(1.03);
    box-shadow: 0 15px 50px #7048ff80;
}

/* TÍTULOS DAS SEÇÕES */

.section-heading {
    text-align: center;
    padding: 20px 20px 35px;
}

.section-heading .eyebrow {
    color: #a78bfa;
    font-size: 11px;
    letter-spacing: 2px;
    font-weight: 800;
    margin-bottom: 12px;
}

.section-heading h2 {
    font-size: clamp(25px, 5vw, 38px);
    font-weight: 900;
}

.section-heading p {
    color: #999bb0;
    font-size: 13px;
    margin-top: 12px;
    line-height: 1.7;
}

/* MEMBROS */

.members {
    max-width: 1050px;
    margin: 0 auto;
    padding: 30px 20px 85px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
}

.member {
    background: #ffffff08;
    border: 1px solid #ffffff18;
    border-radius: 18px;
    padding: 28px 15px;
    text-align: center;
    transition: .3s;
}

.member:hover {
    transform: translateY(-7px);
    border-color: #a78bfa;
    background: #8b5cf612;
}

.member-avatar {
    width: 66px;
    height: 66px;
    margin: 0 auto 15px;
    border-radius: 50%;
    display: grid;
    place-items: center;
    font-size: 25px;
    background: linear-gradient(135deg, #635bdb, #9333ea);
    box-shadow: 0 0 25px #7048ff40;
}

.member h3 {
    font-size: 15px;
    letter-spacing: .5px;
}

.member .role {
    color: #bba7ff;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-top: 8px;
}

/* PRESIDENTE */

.president-wrap {
    max-width: 700px;
    margin: 0 auto;
    padding: 0 20px 75px;
}

.president {
    text-align: center;
    padding: 38px 25px;
    border: 1px solid #d8b4fe70;
    border-radius: 22px;
    background:
        radial-gradient(circle at top, #7048ff30, transparent 65%),
        #ffffff08;
    box-shadow: 0 0 45px #7048ff18;
}

.president .crown {
    font-size: 35px;
    margin-bottom: 12px;
}

.president h3 {
    font-size: 27px;
    font-weight: 900;
}

.president .role {
    color: #d8b4fe;
    font-size: 11px;
    letter-spacing: 2px;
    font-weight: 900;
    margin-top: 9px;
}

/* JOGO */

.games {
    max-width: 950px;
    margin: 0 auto;
    padding: 20px 20px 90px;
}

.game-card {
    display: flex;
    align-items: center;
    gap: 25px;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #ffffff18;
    background: linear-gradient(120deg, #17251d, #101b19);
    transition: .3s;
}

.game-card:hover {
    transform: translateY(-5px);
    border-color: #4ade80;
}

.game-icon {
    flex: 0 0 90px;
    height: 90px;
    display: grid;
    place-items: center;
    border-radius: 18px;
    background: #3b8d4b25;
    font-size: 48px;
}

.game-card h3 {
    font-size: 21px;
    margin-bottom: 8px;
}

.game-card p {
    color: #a1b5a4;
    font-size: 13px;
    line-height: 1.7;
}

.game-label {
    display: inline-block;
    margin-top: 12px;
    padding: 7px 11px;
    border-radius: 30px;
    background: #4ade8018;
    color: #86efac;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
}

/* CONVITE */

.invite {
    text-align: center;
    margin: 0 20px 90px;
    padding: 65px 20px;
    background: linear-gradient(120deg, #191633, #17152b);
    border: 1px solid #8b5cf640;
    border-radius: 25px;
}

.invite h2 {
    font-size: clamp(25px, 5vw, 40px);
    margin-bottom: 15px;
}

.invite p {
    color: #aaa9be;
    margin-bottom: 28px;
    line-height: 1.7;
}

/* RODAPÉ */

footer {
    text-align: center;
    padding: 30px 15px;
    border-top: 1px solid #ffffff12;
    color: #666b80;
    font-size: 11px;
    letter-spacing: 1px;
}

/* BOTÃO DE CHUVA */

.rain-button {
    position: fixed;
    bottom: 25px;
    right: 25px;
    z-index: 10000;
    background: linear-gradient(120deg, #635bdb, #9333ea);
    border: 1px solid #ffffff30;
    color: white;
    padding: 15px 20px;
    border-radius: 14px;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 5px 25px #7048ff55;
    transition: .3s;
}

.rain-button:hover {
    transform: translateY(-4px);
}

.rain-button.active {
    background: linear-gradient(120deg, #312e81, #6b21a8);
}

/* ANIMAÇÕES */

@keyframes float {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-12px);
    }
}

@keyframes shine {
    to {
        background-position: 200% center;
    }
}

/* RESPONSIVIDADE */

@media(max-width: 700px) {
    nav {
        padding: 0 5%;
        height: 72px;
    }

    .logo {
        font-size: 19px;
    }

    .nav-btn {
        font-size: 11px;
        padding: 10px;
    }

    h1 {
        letter-spacing: -2px;
    }

    .hero {
        min-height: 620px;
        padding-top: 70px;
    }

    .hero-orbit {
        transform: scale(.85);
        margin-bottom: 5px;
    }

    .members {
        grid-template-columns: repeat(2, 1fr);
    }

    .game-card {
        align-items: flex-start;
        gap: 16px;
        padding: 18px;
    }

    .game-icon {
        flex-basis: 65px;
        height: 65px;
        font-size: 35px;
    }

    .rain-button {
        bottom: 15px;
        right: 15px;
        padding: 12px 15px;
    }
}

@media(max-width: 380px) {
    .members {
        grid-template-columns: 1fr;
    }
}

@media (hover: none) {
    body {
        cursor: auto;
    }

    .paw-cursor {
        display: none;
    }
}

@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: .01ms !important;
        scroll-behavior: auto !important;
    }
}
</style>
</head>

<body>

<canvas id="spaceCanvas"></canvas>
<canvas id="rainCanvas"></canvas>

<div class="paw-cursor" id="pawCursor">🐾</div>

<nav>
    <a href="#" class="logo">🐶 DOG<span>CHAT</span></a>

    <a href="{{ discord }}" target="_blank"
       rel="noopener noreferrer" class="nav-btn">
        Discord ↗
    </a>
</nav>

<main>

<!-- INÍCIO -->

<section class="hero">

    <div class="glow"></div>

    <div class="hero-orbit" id="heroOrbit">

        <div class="orbit-ring ring-one"></div>
        <div class="orbit-ring ring-two"></div>
        <div class="orbit-ring ring-three"></div>

        <img class="dog"
             src="{{ url_for('static', filename='logo-dois-cachorros.png') }}"
             alt="Logo DOG CHAT">

    </div>

    <div class="tag">
        🐾 SUA NOVA COMUNIDADE TE ESPERA
    </div>

    <h1>
        MAIS QUE UM CHAT.<br>
        <span class="gradient">UMA FAMÍLIA.</span>
    </h1>

    <p class="description">
        Conheça pessoas incríveis, faça amizades,
        converse e divirta-se. O seu lugar é aqui!
    </p>

    <a href="{{ discord }}" target="_blank"
       rel="noopener noreferrer" class="join">
        💬 ENTRAR NO DOG CHAT →
    </a>

</section>

<!-- MEMBROS -->

<section class="section-heading">
    <div class="eyebrow">QUEM FAZ ACONTECER</div>
    <h2>Membros em destaque</h2>
    <p>Quem ajudou a construir a história da comunidade.</p>
</section>

<section class="members">

    <div class="member">
        <div class="member-avatar">🐾</div>
        <h3>NZ99</h3>
        <div class="role">SUPORTE · MEMBRO ANTIGO</div>
    </div>

    <div class="member">
        <div class="member-avatar">🐾</div>
        <h3>ZOLDY</h3>
        <div class="role">SUPORTE · MEMBRO ANTIGO</div>
    </div>

    <div class="member">
        <div class="member-avatar">🐾</div>
        <h3>DIEL</h3>
        <div class="role">SUPORTE · MEMBRO ANTIGO</div>
    </div>

    <div class="member">
        <div class="member-avatar">🐾</div>
        <h3>DNZIN</h3>
        <div class="role">SUPORTE · MEMBRO ANTIGO</div>
    </div>

</section>

<!-- PRESIDENTE -->

<section class="president-wrap">

    <div class="president">
        <div class="crown">👑</div>
        <h3>MANU</h3>
        <div class="role">
            PRESIDENTE DO DOG CHAT
        </div>
    </div>

</section>

<!-- JOGO -->

<section class="section-heading">
    <div class="eyebrow">JOGUE COM A COMUNIDADE</div>
    <h2>Jogo em destaque</h2>
    <p>Uma das aventuras para curtir junto com a galera.</p>
</section>

<section class="games">

    <div class="game-card">

        <div class="game-icon">⛏️</div>

        <div>
            <h3>Minecraft Bedrock</h3>

            <p>
                Construa, explore e sobreviva
                com os membros do DOG CHAT.
            </p>

            <span class="game-label">
                JOGO EM DESTAQUE
            </span>
        </div>

    </div>

</section>

<!-- CONVITE -->

<section class="invite">

    <h2>🐶 VEM PARA O DOG CHAT!</h2>

    <p>
        Estamos esperando por você.<br>
        Clique abaixo e faça parte da nossa comunidade.
    </p>

    <a href="{{ discord }}" target="_blank"
       rel="noopener noreferrer" class="join">
        ENTRAR NA COMUNIDADE ↗
    </a>

</section>

</main>

<footer>
    DOG CHAT © 2026 — FEITO COM 🐾 PARA A COMUNIDADE
</footer>

<!-- ÁUDIO -->

<audio id="rainSound" loop preload="none">
    <source
        src="https://cdn.pixabay.com/audio/2022/05/13/audio_257c3a9c9c.mp3"
        type="audio/mpeg">
</audio>

<button id="rainButton"
        class="rain-button"
        aria-pressed="false">
    🌧️ Ligar chuva
</button>

<script>

/* =================================
   CURSOR DE PATA
================================= */

const pawCursor = document.getElementById("pawCursor");

document.addEventListener("pointermove", function(e) {
    if (e.pointerType !== "mouse") return;

    pawCursor.style.left = e.clientX + "px";
    pawCursor.style.top = e.clientY + "px";
});

document.addEventListener("pointerdown", function() {
    pawCursor.style.transform =
        "translate(-50%, -50%) scale(.75) rotate(-15deg)";
});

document.addEventListener("pointerup", function() {
    pawCursor.style.transform =
        "translate(-50%, -50%) scale(1)";
});


/* =================================
   CHROME ORBIT
================================= */

const heroOrbit = document.getElementById("heroOrbit");

let haloTimer;

heroOrbit.addEventListener("click", function() {

    heroOrbit.classList.remove("halo-active");

    void heroOrbit.offsetWidth;

    heroOrbit.classList.add("halo-active");

    clearTimeout(haloTimer);

    haloTimer = setTimeout(() => {
        heroOrbit.classList.remove("halo-active");
    }, 1900);

});


/* =================================
   LIGHTSPEED - ESTRELAS
================================= */

const spaceCanvas = document.getElementById("spaceCanvas");
const spaceCtx = spaceCanvas.getContext("2d");

let sw, sh, centerX, centerY;
let stars = [];

function resizeSpace() {

    const dpr = Math.min(window.devicePixelRatio || 1, 2);

    sw = window.innerWidth;
    sh = window.innerHeight;

    centerX = sw / 2;
    centerY = sh / 2;

    spaceCanvas.width = sw * dpr;
    spaceCanvas.height = sh * dpr;

    spaceCanvas.style.width = sw + "px";
    spaceCanvas.style.height = sh + "px";

    spaceCtx.setTransform(dpr, 0, 0, dpr, 0, 0);

    stars = [];

    for (let i = 0; i < 150; i++) {
        createStar(true);
    }
}

function createStar(randomDepth = false) {

    stars.push({
        angle: Math.random() * Math.PI * 2,
        depth: randomDepth ? Math.random() : 0.05,
        hue: 245 + Math.random() * 65
    });

}

function animateSpace() {

    spaceCtx.clearRect(0, 0, sw, sh);

    stars.forEach(star => {

        const distance = Math.max(sw, sh);

        const oldX = centerX +
            Math.cos(star.angle) * star.depth * distance;

        const oldY = centerY +
            Math.sin(star.angle) * star.depth * distance;

        star.depth += 0.0035 + star.depth * 0.012;

        const x = centerX +
            Math.cos(star.angle) * star.depth * distance;

        const y = centerY +
            Math.sin(star.angle) * star.depth * distance;

        spaceCtx.beginPath();
        spaceCtx.moveTo(oldX, oldY);
        spaceCtx.lineTo(x, y);

        spaceCtx.strokeStyle =
            `hsla(${star.hue}, 100%, 80%, 0.75)`;

        spaceCtx.lineWidth = Math.min(3, 0.5 + star.depth * 2);
        spaceCtx.stroke();

        if (
            star.depth > 1.15 ||
            x < -40 || x > sw + 40 ||
            y < -40 || y > sh + 40
        ) {
            star.angle = Math.random() * Math.PI * 2;
            star.depth = 0.05;
        }

    });

    requestAnimationFrame(animateSpace);

}

window.addEventListener("resize", resizeSpace);

resizeSpace();
animateSpace();


/* =================================
   CHUVA COM COLISÃO E RESPINGOS
================================= */

const rainCanvas = document.getElementById("rainCanvas");
const rainCtx = rainCanvas.getContext("2d");

const rainButton = document.getElementById("rainButton");
const rainSound = document.getElementById("rainSound");

let rainActive = false;
let drops = [];
let splashes = [];

let rainWidth = 0;
let rainHeight = 0;

function resizeRain() {

    const dpr = Math.min(window.devicePixelRatio || 1, 2);

    rainWidth = window.innerWidth;
    rainHeight = window.innerHeight;

    rainCanvas.width = rainWidth * dpr;
    rainCanvas.height = rainHeight * dpr;

    rainCanvas.style.width = rainWidth + "px";
    rainCanvas.style.height = rainHeight + "px";

    rainCtx.setTransform(dpr, 0, 0, dpr, 0, 0);

}

window.addEventListener("resize", resizeRain);

resizeRain();


function createDrop() {

    drops.push({
        x: Math.random() * rainWidth,
        y: -Math.random() * rainHeight,
        speed: 5 + Math.random() * 4,
        length: 10 + Math.random() * 10,
        width: 1 + Math.random()
    });

}


/* SUPERFÍCIES DE COLISÃO */

function getRainTargets() {

    const selectors = [
        "h1", "h2", "h3", "p",
        "a", "button", ".tag",
        ".eyebrow", ".role",
        ".member-avatar", ".game-icon",
        ".game-card", ".member",
        ".president", ".dog",
        ".logo", ".crown"
    ];

    return [...document.querySelectorAll(selectors.join(","))]
        .filter(element => {

            const rect = element.getBoundingClientRect();
            const style = getComputedStyle(element);

            return (
                rect.width > 0 &&
                rect.height > 0 &&
                style.display !== "none" &&
                style.visibility !== "hidden"
            );

        })
        .map(element => element.getBoundingClientRect());

}


/* RESPINGOS */

function createSplash(x, y) {

    for (let i = 0; i < 6; i++) {

        splashes.push({
            x: x,
            y: y,
            vx: (Math.random() - 0.5) * 4,
            vy: -Math.random() * 3,
            life: 1,
            size: 1 + Math.random() * 2
        });

    }

}


/* ANIMAÇÃO DA CHUVA */

function animateRain() {

    rainCtx.clearRect(0, 0, rainWidth, rainHeight);

    if (rainActive) {

        const targets = getRainTargets();

        if (drops.length < 250) {
            for (let i = 0; i < 5; i++) {
                createDrop();
            }
        }

        for (let i = drops.length - 1; i >= 0; i--) {

            const drop = drops[i];

            const previousY = drop.y;

            drop.y += drop.speed;

            let collided = false;

            for (const target of targets) {

                if (
                    drop.x >= target.left &&
                    drop.x <= target.right &&
                    previousY <= target.top &&
                    drop.y >= target.top &&
                    drop.y <= target.bottom
                ) {

                    createSplash(drop.x, target.top);

                    collided = true;
                    break;

                }

            }

            if (collided || drop.y > rainHeight + 30) {
                drops.splice(i, 1);
                continue;
            }

            rainCtx.beginPath();

            rainCtx.moveTo(drop.x, drop.y);

            rainCtx.lineTo(
                drop.x - 1,
                drop.y - drop.length
            );

            rainCtx.strokeStyle = "rgba(190, 210, 255, 0.75)";
            rainCtx.lineWidth = drop.width;
            rainCtx.stroke();

        }

    }


    /* DESENHA OS RESPINGOS */

    for (let i = splashes.length - 1; i >= 0; i--) {

        const splash = splashes[i];

        splash.x += splash.vx;
        splash.y += splash.vy;

        splash.vy += 0.12;
        splash.life -= 0.055;

        if (splash.life <= 0) {
            splashes.splice(i, 1);
            continue;
        }

        rainCtx.beginPath();

        rainCtx.arc(
            splash.x,
            splash.y,
            splash.size,
            0,
            Math.PI * 2
        );

        rainCtx.fillStyle =
            `rgba(190, 210, 255, ${splash.life})`;

        rainCtx.fill();

    }

    requestAnimationFrame(animateRain);

}

animateRain();


/* =================================
   CONTROLE DO BOTÃO E DO ÁUDIO
================================= */

rainSound.volume = 0.25;

rainButton.addEventListener("click", async function() {

    if (!rainActive) {

        rainActive = true;

        rainButton.textContent = "🔊 Desligar chuva";

        rainButton.classList.add("active");

        rainButton.setAttribute("aria-pressed", "true");

        try {
            await rainSound.play();
        } catch (error) {
            console.warn("O áudio da chuva não pôde ser reproduzido.", error);
        }

    } else {

        rainActive = false;

        rainButton.textContent = "🌧️ Ligar chuva";

        rainButton.classList.remove("active");

        rainButton.setAttribute("aria-pressed", "false");

        rainSound.pause();

        rainSound.currentTime = 0;

        drops = [];
        splashes = [];

    }

});

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML, discord=DISCORD)


if __name__ == "__main__":
    app.run(debug=True)
