document.getElementById('uploadForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    const formData = new FormData();
    const audioFile = document.getElementById('audioFile').files[0];
    const firstSpeaker = document.getElementById('firstSpeaker').value;

    if (!audioFile || !firstSpeaker) {
        alert('Por favor, preencha todos os campos!');
        return;
    }

    formData.append('file', audioFile);
    formData.append('firstSpeaker', firstSpeaker);

    try {
        const response = await fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (response.ok) {
            // Preenche a área de transcrição com a resposta da transcrição e diarização
            const transcriptionArea = document.getElementById('transcription');
            transcriptionArea.value = formatTranscription(result);
        } else {
            alert('Erro ao processar o áudio: ' + result.error);
        }
    } catch (error) {
        console.error('Erro ao enviar áudio:', error);
        alert('Erro ao enviar áudio');
    }
});

// Função para formatar a transcrição
function formatTranscription(data) {
    let formattedText = "Transcrição e Diarização:\n\n";
    
    if (data && data.segments) {
        data.segments.forEach(segment => {
            formattedText += `${segment.speaker}: ${segment.text}\n`;
        });
    } else {
        formattedText = "Nenhuma transcrição ou diarização foi gerada.";
    }
    
    return formattedText;
}
