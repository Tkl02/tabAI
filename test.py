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
