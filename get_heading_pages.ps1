$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open("E:\Project Report\Adaptive_MultiAgent_GraphRAG_Project_Report_Stage1.docx")
$results = @()
foreach ($p in $doc.Paragraphs) {
    $txt = $p.Range.Text.Trim()
    if ($txt -match "^[1-8]\.[0-9]" -or $txt -match "^CHAPTER") {
        $pg = $p.Range.Information(3) # absolute page
        # In section 2, relative page is $pg - 10
        $rel_pg = $pg - 10
        if ($rel_pg -lt 1) { $rel_pg = 1 }
        $results += "$txt :: $rel_pg"
    }
}
$doc.Close([ref]$false)
$word.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
$results | Out-File -FilePath "heading_page_numbers.txt" -Encoding utf8
Write-Output "Extracted $($results.Count) headings to heading_page_numbers.txt"
