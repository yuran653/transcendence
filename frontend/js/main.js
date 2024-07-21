document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/databases/')
        .then(response => {
            if (!response.ok) {
                throw new Error('No available databases');
            }
            return response.json();
        })
        .then(data => {
            const list = document.getElementById('database-list');
            data.databases.forEach(db => {
                const listItem = document.createElement('li');
                listItem.textContent = db;
                list.appendChild(listItem);
            });
        })
        .catch(error => {
            const list = document.getElementById('database-list');
            const listItem = document.createElement('li');
            listItem.textContent = error.message;
            list.appendChild(listItem);
        });
});
