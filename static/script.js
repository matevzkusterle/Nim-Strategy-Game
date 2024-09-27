// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function() {
    const gameID = "{{id}}";  // Assuming this ID is rendered in the HTML

    // Periodically check for game state updates
    setInterval(checkForUpdates, 5000);

    function checkForUpdates() {
        fetch(`/game-state/${gameID}`)
            .then(response => response.json())
            .then(data => {
                if (data.updated) {
                    // Update the game board if there are changes
                    document.getElementById("first-row").innerHTML = data.first;
                    document.getElementById("second-row").innerHTML = data.second;
                    document.getElementById("third-row").innerHTML = data.third;
                }
            })
            .catch(error => console.error('Error:', error));
    }

    // Form validation before submission
    const form = document.getElementById("move-form");

    form.addEventListener("submit", function(event) {
        const rowInput = document.getElementById("row");
        const countInput = document.getElementById("count");

        const row = parseInt(rowInput.value);
        const count = parseInt(countInput.value);

        if (isNaN(row) || isNaN(count) || row < 0 || row > 2 || count <= 0) {
            alert("Please enter valid row and count values.");
            event.preventDefault();
        }
    });
});
