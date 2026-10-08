$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open("E:\Project Report\Adaptive_MultiAgent_GraphRAG_Project_Report_Stage1.docx")
foreach ($p in $doc.Paragraphs) {
    $txt = $p.Range.Text.Trim()
    if ($txt -match "^CHAPTER" -or $txt -match "^CERTIFICATE" -or $txt -match "^ACKNOWLEDGEMENT" -or $txt -match "^ABSTRACT" -or $txt -match "^TABLE OF CONTENTS" -or $txt -match "^LIST OF") {
        $pg = $p.Range.Information(3)
        Write-Output "Page $pg : $txt"
    }
}
$doc.Close([ref]$false)
$word.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
