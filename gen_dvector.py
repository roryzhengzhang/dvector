import torch
import torchaudio

wav2mel = torch.jit.load("checkpoint/wav2mel.pt")
dvector = torch.jit.load("checkpoint/dvector-step250000.pt").eval()

wav_tensor, sample_rate = torchaudio.load("example/nora2092_6.wav")
mel_tensor = wav2mel(wav_tensor, sample_rate)  # shape: (frames, mel_dim)
emb_tensor = dvector.embed_utterance(mel_tensor)  # shape: (emb_dim)

print(f"emb_vector: {emb_tensor}")
print(f"emb size: {emb_tensor.size()}")