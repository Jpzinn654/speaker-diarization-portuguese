document.getElementById('uploadForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    const formData = new FormData();
    const audioFile = document.getElementById('audioFile').files[0];
    const firstSpeaker = document.getElementById('firstSpeaker').value; // Captura o valor selecionado

    if (!audioFile || firstSpeaker === "") {
        alert('Por favor, preencha todos os campos!');
        return;
    }

    // Mostra o spinner e desabilita a interação
    document.getElementById('spinner').classList.remove('hidden'); // Mostra o spinner
    document.getElementById('uploadForm').querySelector('button').disabled = true; // Desabilita o botão
    document.getElementById('audioFile').disabled = true; // Desabilita o input de arquivo
    document.getElementById('firstSpeaker').disabled = true; // Desabilita o seletor do locutor

    formData.append('file', audioFile);
    formData.append('firstSpeaker', firstSpeaker); // Envia o valor do primeiro locutor

    try {
        // Envia o formulário via POST para o Flask
        const response = await fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (response.ok) {
            // Preenche a área de transcrição com a resposta da transcrição e diarização
            const transcriptionArea = document.getElementById('transcription');
            transcriptionArea.value = formatTranscription(result);

            // Esconde o spinner e reabilita a interação
            document.getElementById('spinner').classList.add('hidden'); // Esconde o spinner
            document.getElementById('uploadForm').querySelector('button').disabled = false; // Habilita o botão
            document.getElementById('audioFile').disabled = false; // Habilita o input de arquivo
            document.getElementById('firstSpeaker').disabled = false; // Habilita o seletor do locutor
        } else {
            alert('Erro ao processar o áudio: ' + result.error);
            // Esconde o spinner e reabilita a interação em caso de erro
            document.getElementById('spinner').classList.add('hidden');
            document.getElementById('uploadForm').querySelector('button').disabled = false;
            document.getElementById('audioFile').disabled = false;
            document.getElementById('firstSpeaker').disabled = false;
        }
    } catch (error) {
        console.error('Erro ao enviar áudio:', error);
        alert('Erro ao enviar áudio');
        // Esconde o spinner e reabilita a interação em caso de erro
        document.getElementById('spinner').classList.add('hidden');
        document.getElementById('uploadForm').querySelector('button').disabled = false;
        document.getElementById('audioFile').disabled = false;
        document.getElementById('firstSpeaker').disabled = false;
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
