import gradio as gr
import joblib
import numpy as np
from feature_extraction import extract_features
from matcher import recommend_tracks
from database import log_query

# Load models
model = joblib.load("model/mood_model.pkl")
encoder = joblib.load("model/label_encoder.pkl")

def process(audio_path):
    """Process audio and return comprehensive analysis."""
    try:
        if audio_path is None:
            return {
                "mood": "Waiting",
                "confidence": "0%",
                "bpm": "0",
                "tracks": "Upload an audio file",
                "color": "#6B7280",
                "icon": "⏳"
            }
        
        features, bpm = extract_features(audio_path)
        
        if features is None:
            return {
                "mood": "Error",
                "confidence": "0%",
                "bpm": "0",
                "tracks": "Failed to process",
                "color": "#EF4444",
                "icon": "❌"
            }
        
        features = np.array(features).reshape(1, -1)
        probs = model.predict_proba(features)[0]
        mood_idx = np.argmax(probs)
        confidence = float(probs[mood_idx])
        
        if confidence < 0.55:
            mood, color, icon = "Uncertain", "#9CA3AF", "❓"
            mood_label = "uncertain"
        else:
            mood_label = encoder.inverse_transform([mood_idx])[0]
            config = {
                "happy": ("Happy", "#FBBF24", "😊"),
                "calm": ("Calm", "#60A5FA", "😌"),
                "energetic": ("Energetic", "#EC4899", "⚡"),
                "sad": ("Melancholic", "#A78BFA", "😢")
            }
            mood, color, icon = config.get(mood_label, (mood_label.title(), "#6B7280", "🎵"))
        
        try:
            results = recommend_tracks(
                input_features=features.flatten(),
                input_bpm=bpm,
                input_mood=mood_label,
                weight=0.5
            )
            tracks_str = "\n".join(f"• {t}" for t in results["track_id"].tolist()) if results is not None and len(results) > 0 else "No recommendations"
        except:
            tracks_str = "Unable to load recommendations"
        
        try:
            log_query(mood_label, bpm, results["track_id"].tolist() if 'results' in locals() else [])
        except:
            pass
        
        return {
            "mood": mood,
            "icon": icon,
            "confidence": f"{confidence*100:.0f}%",
            "bpm": f"{bpm:.0f}",
            "tracks": tracks_str,
            "color": color
        }
    
    except:
        return {
            "mood": "Error",
            "confidence": "0%",
            "bpm": "0",
            "tracks": "An error occurred",
            "color": "#EF4444",
            "icon": "❌"
        }

# Premium CSS - Glassmorphism with Animations
premium_css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

:root {
    --accent: #3B82F6;
    --accent-light: #60A5FA;
}

* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

body {
    background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0F172A 100%);
    background-attachment: fixed;
    overflow-x: hidden;
}

.gradio-container {
    max-width: 1400px !important;
    margin: 0 auto !important;
    padding: 32px 20px !important;
    background: transparent !important;
}

.header-logo {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -0.02em;
    text-align: center;
    margin-bottom: 12px;
    animation: fadeInDown 0.8s ease-out;
}

.header-tagline {
    font-size: 1.1rem;
    color: rgba(255, 255, 255, 0.7);
    text-align: center;
    letter-spacing: 0.05em;
    margin-bottom: 48px;
}

.glass-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 16px;
    padding: 32px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-card:hover {
    background: rgba(255, 255, 255, 0.12);
    border-color: rgba(255, 255, 255, 0.25);
    transform: translateY(-4px);
    box-shadow: 0 20px 25px -5px rgba(59, 130, 246, 0.2);
}

button {
    font-family: 'Inter', sans-serif !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    padding: 12px 24px !important;
    border: none !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    position: relative;
    overflow: hidden;
}

button::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    transition: width 0.6s, height 0.6s;
    z-index: -1;
}

button:hover::before {
    width: 300px;
    height: 300px;
}

.btn-primary {
    background: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%) !important;
    color: white !important;
    box-shadow: 0 10px 20px rgba(59, 130, 246, 0.3) !important;
}

.btn-primary:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 15px 30px rgba(59, 130, 246, 0.4) !important;
}

.btn-secondary {
    background: rgba(255, 255, 255, 0.1) !important;
    color: white !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
}

.btn-secondary:hover {
    background: rgba(255, 255, 255, 0.15) !important;
    border-color: rgba(255, 255, 255, 0.4) !important;
}

.result-label {
    font-size: 0.8rem;
    color: rgba(255, 255, 255, 0.6);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 8px;
    font-weight: 600;
}

.result-value {
    font-size: 2.5rem;
    font-weight: 800;
    color: white;
    margin-bottom: 8px;
    letter-spacing: -0.02em;
}

.mood-badge {
    display: inline-block;
    padding: 12px 24px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 1.1rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 16px;
    backdrop-filter: blur(10px);
    color: white;
    animation: pulse 2s ease-in-out infinite;
}

.visualizer {
    height: 60px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    gap: 4px;
    padding: 16px 8px;
    margin: 16px 0;
}

.bar {
    width: 4px;
    background: linear-gradient(180deg, var(--accent), #8B5CF6);
    border-radius: 2px;
    animation: wave 0.6s ease-in-out infinite;
}

@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.8; }
}

@keyframes wave {
    0%, 100% { height: 20%; }
    50% { height: 100%; }
}

@keyframes slideInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

h1, h2, h3 {
    color: white !important;
    font-weight: 700 !important;
}

p, .gr-markdown {
    color: rgba(255, 255, 255, 0.8) !important;
}

.gr-textbox input,
.gr-textbox textarea {
    background: rgba(255, 255, 255, 0.08) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    font-size: 0.95rem !important;
}

.gr-textbox input:focus,
.gr-textbox textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2) !important;
    background: rgba(255, 255, 255, 0.12) !important;
}

.info-box {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 16px;
    padding: 32px;
    margin-top: 48px;
    animation: slideInUp 0.6s ease-out 0.2s both;
}

@media (max-width: 768px) {
    .gradio-container {
        padding: 20px 12px !important;
    }
    
    .header-logo {
        font-size: 2rem;
    }
    
    .result-value {
        font-size: 2rem;
    }
    
    .glass-card {
        padding: 20px;
    }
}

@media (prefers-reduced-motion: reduce) {
    * {
        animation: none !important;
        transition: none !important;
    }
}
/* Animated gradient backgrounds */
.animated-bg {
    background: linear-gradient(120deg, #0ea5e9 0%, #8b5cf6 25%, #f97316 50%, #ef4444 75%, #06b6d4 100%);
    background-size: 300% 300%;
    animation: gradientShift 12s ease infinite;
}

@keyframes gradientShift {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
}

/* Dropzone */
.dropzone {
    border: 2px dashed rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 24px;
    text-align: center;
    color: rgba(255,255,255,0.8);
    transition: border-color 0.2s ease, transform 0.12s ease;
}
.dropzone.dragover {
    border-color: var(--accent);
    transform: translateY(-4px);
}

/* Canvas visualizer */
#visualizer_canvas { width:100%; height:140px; border-radius:12px; background: rgba(255,255,255,0.03); display:block }

/* Progress */
.progress { height: 10px; background: rgba(255,255,255,0.06); border-radius: 999px; overflow: hidden; }
.progress > .bar { height:100%; width:0%; background: linear-gradient(90deg,var(--accent), #8B5CF6); transition: width 300ms linear }

/* Sidebar / history */
.sidebar { background: rgba(255,255,255,0.03); border-left: 1px solid rgba(255,255,255,0.04); padding: 18px; border-radius: 12px }
.history-item { padding: 12px; border-radius: 10px; margin-bottom: 8px; background: rgba(255,255,255,0.02); cursor: pointer }

/* Export button */
.export-btn { background: rgba(255,255,255,0.06); color: white; border-radius: 10px; padding: 8px 12px; border: none }

/* Light theme */
:root[data-theme='light'] { --bg: #F8FAFC; --text: #0F172A; }
body[data-theme='light'] { background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 50%); color: var(--text) }

"""

# Create UI
with gr.Blocks(theme=gr.themes.Soft(), analytics_enabled=False) as ui:
    gr.HTML('<div class="header-logo">🎵 PLAYMOOD</div>')
    gr.HTML('<div class="header-tagline">Professional Audio Mood Analysis • Powered by AI</div>')
    
    with gr.Row():
        with gr.Column(scale=1.2):
            gr.HTML('<h2 style="color: white; margin-bottom: 16px;">📤 Upload Track</h2>')
            
            with gr.Group(elem_classes="glass-card"):
                gr.HTML('<div class="dropzone" id="dropzone">Drag & drop audio here or click to select<br><small>MP3 / WAV up to 10MB</small></div>')
                audio_input = gr.Audio(type="filepath", label="Select Audio File", container=True)
                gr.HTML('<canvas id="visualizer_canvas"></canvas>')
                gr.HTML('<div style="margin-top:8px" class="progress"><div class="bar" id="analysis_bar"></div></div>')
                with gr.Row():
                    submit_btn = gr.Button("▶ Analyze", scale=2, variant="primary", elem_classes="btn-primary")
                    clear_btn = gr.Button("↻ Reset", scale=1, elem_classes="btn-secondary")
                    export_btn = gr.Button("⬇ Export PNG", scale=1, elem_classes="export-btn")
        
        with gr.Column(scale=1.2):
            gr.HTML('<h2 style="color: white; margin-bottom: 16px;">📊 Results</h2>')
            
            with gr.Group(elem_classes="glass-card"):
                mood_badge = gr.HTML('<div class="mood-badge" id="mood_badge" style="background: linear-gradient(135deg, #6B7280, #4B5563);">⏳ Waiting</div>')
                
                with gr.Row():
                    with gr.Column():
                        gr.HTML('<div class="result-label">Mood</div>')
                        mood_output = gr.Textbox(interactive=False, container=False, show_label=False, elem_classes="result-value")
                    
                    with gr.Column():
                        gr.HTML('<div class="result-label">Confidence</div>')
                        confidence_output = gr.Textbox(interactive=False, container=False, show_label=False, elem_classes="result-value")
                    
                    with gr.Column():
                        gr.HTML('<div class="result-label">Tempo</div>')
                        bpm_output = gr.Textbox(interactive=False, container=False, show_label=False, elem_classes="result-value")
                
                gr.HTML('<div class="visualizer"><div class="bar" style="animation-delay: 0s"></div><div class="bar" style="animation-delay: 0.1s"></div><div class="bar" style="animation-delay: 0.2s"></div><div class="bar" style="animation-delay: 0.3s"></div><div class="bar" style="animation-delay: 0.4s"></div></div>')
                
                gr.HTML('<div class="result-label" style="margin-top: 16px;">Recommended Tracks</div>')
                tracks_output = gr.Textbox(interactive=False, container=False, show_label=False, lines=4, placeholder="Recommendations will appear here...", elem_classes="result-value")
                gr.HTML('<div id="lottie_mood" style="width:80px; height:80px; margin-top:8px"></div>')
                mood_meta = gr.HTML('<div id="mood_meta" style="display:none"></div>')
    
    gr.HTML('<div class="info-box"><h3 style="color: white; margin-bottom: 16px;">🚀 How It Works</h3><p style="color: rgba(255, 255, 255, 0.8); line-height: 1.8; margin-bottom: 0;">Upload an MP3 or WAV file → AI analyzes advanced audio features (MFCC, tempo, energy, rhythm) → Deep learning model classifies mood with confidence → Personalized track recommendations from catalog. Built with signal processing & machine learning.</p></div>')
    
    color_state = gr.State("#6B7280")
    
    def handle_analysis(audio_path):
        result = process(audio_path)
        badge = f'<div class="mood-badge" style="background: linear-gradient(135deg, {result["color"]}, {result["color"]}dd); color: white;">{result["icon"]} {result["mood"]}</div>'
        # hidden meta for frontend JS hooks
        meta = f'<div id="mood_meta" data-mood="{result.get("mood","")}" data-color="{result.get("color","#6B7280")}" data-confidence="{result.get("confidence","0%")}"></div>'
        return result["mood"], result["confidence"], result["bpm"], result["tracks"], badge, result["color"], meta
    
    submit_btn.click(
        handle_analysis,
        inputs=audio_input,
        outputs=[mood_output, confidence_output, bpm_output, tracks_output, mood_badge, color_state, mood_meta]
    )
    
    clear_btn.click(
        lambda: (None, "", "", "", '<div class="mood-badge" style="background: linear-gradient(135deg, #6B7280, #4B5563);">⏳ Waiting</div>', "#6B7280", '<div id="mood_meta"></div>'),
        outputs=[audio_input, mood_output, confidence_output, bpm_output, tracks_output, mood_badge, color_state, mood_meta]
    )

    # Add supporting scripts (Lottie, html2canvas, visualizer wiring)
    gr.HTML('''
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.7.13/lottie.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script>
    (()=>{
        const fileInput = document.querySelector('input[type=file]');
        const drop = document.getElementById('dropzone');
        const canvas = document.getElementById('visualizer_canvas');
        const progressBar = document.getElementById('analysis_bar');
        const lottieContainer = document.getElementById('lottie_mood');
        let audioCtx, analyser, dataArray, sourceNode, audioEl, rafId;

        function initVisualizer(file) {
            if(!file) return;
            if(rafId) cancelAnimationFrame(rafId);
            if(audioEl) { audioEl.pause(); audioEl.src = ''; }
            audioEl = new Audio(URL.createObjectURL(file));
            audioEl.crossOrigin = 'anonymous';
            audioEl.controls = false;

            audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            analyser = audioCtx.createAnalyser();
            analyser.fftSize = 2048;
            const bufferLength = analyser.frequencyBinCount;
            dataArray = new Uint8Array(bufferLength);

            sourceNode = audioCtx.createMediaElementSource(audioEl);
            sourceNode.connect(analyser);
            analyser.connect(audioCtx.destination);

            const dpr = window.devicePixelRatio || 1;
            canvas.width = canvas.clientWidth * dpr;
            canvas.height = canvas.clientHeight * dpr;
            const ctx = canvas.getContext('2d');
            ctx.scale(dpr, dpr);

            function draw(){
                analyser.getByteTimeDomainData(dataArray);
                ctx.clearRect(0,0,canvas.clientWidth, canvas.clientHeight);
                ctx.fillStyle = 'rgba(255,255,255,0.03)';
                ctx.fillRect(0,0,canvas.clientWidth, canvas.clientHeight);
                ctx.lineWidth = 2;
                ctx.strokeStyle = 'rgba(255,255,255,0.9)';
                ctx.beginPath();
                const sliceWidth = canvas.clientWidth / dataArray.length;
                let x = 0;
                for(let i=0;i<dataArray.length;i++){
                    const v = dataArray[i] / 128.0;
                    const y = v * canvas.clientHeight/2;
                    if(i===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
                    x += sliceWidth;
                }
                ctx.lineTo(canvas.clientWidth, canvas.clientHeight/2);
                ctx.stroke();
                rafId = requestAnimationFrame(draw);
            }
            audioEl.play();
            draw();
        }

        if(drop){
            drop.addEventListener('click', ()=> fileInput && fileInput.click());
            ['dragenter','dragover'].forEach(ev=> drop.addEventListener(ev, (e)=>{ e.preventDefault(); drop.classList.add('dragover'); }));
            ['dragleave','drop'].forEach(ev=> drop.addEventListener(ev, (e)=>{ e.preventDefault(); drop.classList.remove('dragover'); }));
            drop.addEventListener('drop', (e)=>{
                const f = e.dataTransfer.files[0];
                if(f && fileInput){
                    const dt = new DataTransfer(); dt.items.add(f); fileInput.files = dt.files;
                    initVisualizer(f);
                }
            });
        }

        if(fileInput){
            fileInput.addEventListener('change', ()=>{
                const f = fileInput.files && fileInput.files[0];
                if(f) initVisualizer(f);
            });
        }

        // Observe mood meta and update UI hooks (progress -> success, lottie)
        const observer = new MutationObserver((mutations)=>{
            for(const m of mutations){
                if(m.type==='childList' && m.addedNodes.length){
                    const node = m.addedNodes[0];
                    if(node && node.dataset){
                        const mood = node.dataset.mood || 'Waiting';
                        const color = node.dataset.color || '#6B7280';
                        // animate progress to 100%
                        progressBar.style.width = '100%';
                        setTimeout(()=> progressBar.style.width = '0%', 1200);
                        // load a simple lottie animation per mood (placeholder shapes)
                        if(window.lottie){
                            lottieContainer.innerHTML = '';
                            let path = 'https://assets9.lottiefiles.com/packages/lf20_tfb3estd.json';
                            if(mood.toLowerCase().includes('happy')) path = 'https://assets2.lottiefiles.com/packages/lf20_jtbfg2nb.json';
                            if(mood.toLowerCase().includes('calm')) path = 'https://assets6.lottiefiles.com/packages/lf20_jz6z2d7c.json';
                            if(mood.toLowerCase().includes('energetic')) path = 'https://assets9.lottiefiles.com/packages/lf20_sSF6EG.json';
                            if(mood.toLowerCase().includes('melancholic')||mood.toLowerCase().includes('sad')) path = 'https://assets7.lottiefiles.com/packages/lf20_mf2z1rwl.json';
                            lottie.loadAnimation({ container: lottieContainer, renderer: 'svg', loop:true, autoplay:true, path });
                        }
                    }
                }
            }
        });
        const moodMetaEl = document.getElementById('mood_meta');
        if(moodMetaEl) observer.observe(moodMetaEl, { childList:true });

        // Export PNG
        const exportBtn = document.querySelector('.export-btn');
        exportBtn && exportBtn.addEventListener('click', ()=>{
            const target = document.querySelector('.glass-card');
            html2canvas(target, {useCORS:true, backgroundColor:null}).then(canvas=>{
                const a = document.createElement('a'); a.download='playmood_result.png'; a.href=canvas.toDataURL('image/png'); a.click();
            });
        });
    })();
    </script>
    ''')

ui.launch(server_name="127.0.0.1", server_port=7860, show_error=True, css=premium_css)
