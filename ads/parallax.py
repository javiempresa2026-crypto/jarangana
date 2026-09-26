"""Anima una foto fija con efecto 3D (paralaje) usando un mapa de profundidad (Depth Anything V2, ONNX).
Uso: parallax.py foto.jpg salida.mp4 [segundos] [movimiento: push|pan|tilt]"""
import sys, subprocess, numpy as np, cv2, onnxruntime as ort, os
MODEL = os.environ.get("DEPTH_MODEL", "/tmp/claude-0/-home-user-jaranga/3c1af52d-99f0-5bf1-b1fa-f77bd1255c3c/scratchpad/depth/depth.onnx")
W, H, FPS = 1080, 1920, 30

def depth_map(img):
    h, w = img.shape[:2]; s = 518 / max(h, w)
    nh, nw = int(h * s) // 14 * 14, int(w * s) // 14 * 14
    x = cv2.resize(img, (nw, nh))[:, :, ::-1].astype(np.float32) / 255
    x = (x - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]
    x = x.transpose(2, 0, 1)[None].astype(np.float32)
    d = ort.InferenceSession(MODEL).run(None, {"pixel_values": x})[0][0]
    d = cv2.resize(d, (w, h)); d = (d - d.min()) / (d.max() - d.min() + 1e-6)
    return cv2.GaussianBlur(d, (0, 0), 3)   # 1 = cerca

def render(src, out, secs=4.0, move="push"):
    img = cv2.imread(src)
    # llenar 9:16
    h, w = img.shape[:2]; s = max(W / w, H / h) * 1.08
    img = cv2.resize(img, (int(w * s), int(h * s)), interpolation=cv2.INTER_LANCZOS4)
    d = depth_map(img)
    h, w = img.shape[:2]
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    cx, cy = (w - W) / 2, (h - H) / 2
    n = int(secs * FPS)
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    dc = d[int(cy):int(cy) + H, int(cx):int(cx) + W]
    for i in range(n):
        t = i / (n - 1); e = t * t * (3 - 2 * t)   # suavizado
        if move == "push":   # la cámara avanza: lo cercano crece más
            z = 0.06 * e; mx = xx + cx - (xx - W / 2) * z * dc * 1.6; my = yy + cy - (yy - H / 2) * z * dc * 1.6
            mx -= (xx - W / 2) * 0.03 * e; my -= (yy - H / 2) * 0.03 * e
        elif move == "pan":
            off = (e - 0.5) * 60; mx = xx + cx + off * dc; my = yy + cy
        else:
            off = (e - 0.5) * 60; mx = xx + cx; my = yy + cy + off * dc
        # temblor leve de móvil en mano
        mx += np.sin(i * 0.35) * 1.5; my += np.cos(i * 0.27) * 1.5
        fr = cv2.remap(img, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
        p.stdin.write(fr.tobytes())
    p.stdin.close(); p.wait(); print("ok", out)

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 4.0, sys.argv[4] if len(sys.argv) > 4 else "push")
