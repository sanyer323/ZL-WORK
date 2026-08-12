
$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
Add-Type -AssemblyName System.Speech
$s = New-Object System.Speech.Synthesis.SpeechSynthesizer
$zh = $s.GetInstalledVoices() | ForEach-Object { $_.VoiceInfo } | Where-Object { $_.Culture.Name -like 'zh*' } | Select-Object -First 1
if ($zh) { $s.SelectVoice($zh.Name) }
$s.Rate = -1
$text = [System.IO.File]::ReadAllText('C:\Users\sanye\Desktop\SMAR\AI研发产品\研发仿真视频\out\_principle_build\_tts.txt', [System.Text.Encoding]::UTF8)
$s.SetOutputToWaveFile('C:\Users\sanye\Desktop\SMAR\AI研发产品\研发仿真视频\out\_principle_build\take_4.wav')
$s.Speak($text)
$s.Dispose()
