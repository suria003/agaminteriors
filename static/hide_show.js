function contactDataFetch(){
    const contactDataInfo = document.getElementById('contact-data').style.display='block';
}

function estimateDataFetch(){
    const estimateDataFetch = document.getElementById('estimate-data').style.display='block';
}

function closeBarContactbtn(){
    const contactDataHide = document.getElementById('contact-data').style.display='none';
}

function closeBarEstimate(){
    const estimateDataFetch = document.getElementById('estimate-data').style.display='none';
}

function showTheKitchenPayment(){
    const showThekitchenPaymentColumn = document.getElementById('kitchenProductPaymentInfo').style.display='flex';
    const hideThekitchenProductColumn = document.getElementById('kitchenProduct').style.display='none';
    const backButton = document.getElementById('backToButton').style.display='flex';
}

function showTheKitchenProduct(){
    const showThekitchenContent = document.getElementById('kitchenProductPaymentInfo').style.display='none';
    const backButton = document.getElementById('backToButton').style.display='none';
    const viewProductPanel = document.getElementById('kitchenProduct').style.display='flex';
}