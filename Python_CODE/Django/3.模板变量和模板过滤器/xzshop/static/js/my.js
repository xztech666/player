setInterval(function() {
        var now = new Date();
        var formattedDate = now.getFullYear() + '-' + (now.getMonth() + 1) + '-' + now.getDate() + ' ' + now.getHours() + ':' + now.getMinutes() + ':' + now.getSeconds();
        document.getElementById('current-time').innerHTML = formattedDate;
    }, 1000); // 1000 milliseconds = 1 second

// alert("hello!!")