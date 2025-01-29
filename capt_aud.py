from pydub import AudioSegment
import subprocess

input_file_path = (r'audiotest\Supermodel.mp4')

# Função para converter MP4 para MP3
def convert_mp4_to_mp3(input_path):
    output_path = input_path.replace('.mp4', '.mp3')
    audio = AudioSegment.from_file(input_path, format="mp4")
    audio.export(output_path, format="mp3")
    print(f"Arquivo convertido para MP3: {output_path}")
    return output_path

# Função para converter WAV para MP3
def convert_wav_to_mp3(input_path):
    output_path = input_path.replace('.wav', '.mp3')
    audio = AudioSegment.from_file(input_path, format="wav")
    audio.export(output_path, format="mp3")
    print(f"Arquivo convertido para MP3: {output_path}")
    return output_path

def extract_instruments():
    import subprocess

    # Caminho do arquivo MP3 de entrada (verifique se o formato é válido para o Demucs)
    input_audio = 'audiotest\\Supermodel.wav'  # Ou 'Supermodel.mp3' se for MP3

    # Diretório de saída
    output_dir = 'demucs_output'

    # Comando para executar o Demucs
    command = f"demucs --out {output_dir} {input_audio}"

    # Executa o Demucs para separar os instrumentos
    subprocess.run(command, shell=True)

    print(f"Arquivos separados salvos em: {output_dir}")

