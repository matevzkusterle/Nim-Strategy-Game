// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    const gameID = "{{id}}"; // Assuming this ID is rendered in the HTML

    // Periodically check for game state updates
    const updateInterval = setInterval(checkForUpdates, 5000);

    /**
     * Fetches the latest game state from the server and updates the board if necessary.
     */
    function checkForUpdates() {
        fetch(`/game-state/${gameID}`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then((data) => {
                if (data.updated) {
                    // Update the game board with the new state
                    document.getElementById("first-row").textContent = data.first;
                    document.getElementById("second-row").textContent = data.second;
                    document.getElementById("third-row").textContent = data.third;
                }
            })
            .catch((error) => {
                console.error("Error fetching game state:", error);
            });
    }

    // Form validation before submission
    const form = document.getElementById("move-form");

    form.addEventListener("submit", function (event) {
        const rowInput = document.getElementById("row");
        const countInput = document.getElementById("count");

        const row = parseInt(rowInput.value);
        const count = parseInt(countInput.value);

        // Validate row and count inputs
        if (isNaN(row) || isNaN(count) || row < 0 || row > 2 || count <= 0) {
            alert("Please enter valid row and count values.");
            event.preventDefault(); // Prevent form submission if validation fails
        }
    });

    // Cleanup interval when the page is unloaded (optional)
    window.addEventListener("beforeunload", function () {
        clearInterval(updateInterval);
    });
});