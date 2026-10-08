try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $doc = $word.Documents.Open("E:\Project Report\Adaptive_MultiAgent_GraphRAG_Project_Report_Stage1.docx")
    $pages = $doc.ComputeStatistics(2)
    $words = $doc.ComputeStatistics(0)
    $doc.Close([ref]$false)
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
    Write-Output "SUCCESS: Pages = $pages, Words = $words"
} catch {
    Write-Output "INFO: MS Word COM is not installed on this machine: $_"
}
