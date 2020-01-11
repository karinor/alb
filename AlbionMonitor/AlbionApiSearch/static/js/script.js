function search()
{
    var req = document.search.req
    request.open("GET", "http://localhost:8080/?q"+req);
    request.onreadystatechange = reqReadyStateChange;
    request.send();
}