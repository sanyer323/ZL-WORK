
$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
Add-Type -AssemblyName System.Speech
$s = New-Object System.Speech.Synthesis.SpeechSynthesizer
$voices = $s.GetInstalledVoices() | ForEach-Object { $_.VoiceInfo }
$zh = $voices | Where-Object { $_.Culture.Name -like 'zh*' } | Select-Object -First 1
if ($zh) { $s.SelectVoice($zh.Name) }
$s.Rate = -1
$text = [System.IO.File]::ReadAllText('C:\Users\sanye\Desktop\SMAR\AI研发产品\研发仿真视频\out\_build\_tts_text.txt', [System.Text.Encoding]::UTF8)
$s.SetOutputToWaveFile('C:\Users\sanye\Desktop\SMAR\AI研发产品\研发仿真视频\out\_build\sapi_narr_4.wav')
$s.Speak($text)
$s.Dispose()
