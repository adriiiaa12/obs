document.addEventListener('DOMContentLoaded', () => {
    const newsContainer = document.getElementById('news-container');
    
    const newsArticles = [
        // NOTICIAS
        {
            title: 'Diario Fin De Mes',
            description: 'Actualizaciones y noticias del mes de mayo. Nuevas construcciones e inauguraciones de la facción. ',
            date: '30-05-2024',
            imagePath: 'images/noticia_1.png'
        }
    ];

    newsArticles.forEach(article => {
        const newsItem = document.createElement('div');
        newsItem.className = 'news-item';

        const title = document.createElement('h2');
        title.textContent = article.title;
        newsItem.appendChild(title);

        const description = document.createElement('p');
        description.textContent = article.description;
        newsItem.appendChild(description);

        const newsFooter = document.createElement('div');
        newsFooter.className = 'news-footer';

        const date = document.createElement('div');
        date.className = 'date';
        date.textContent = article.date;
        newsFooter.appendChild(date);

        const link = document.createElement('a');
        link.href = article.imagePath;
        link.target = '_blank';
        link.className = 'news-link';
        link.textContent = 'Ver Noticia';
        newsFooter.appendChild(link);

        newsItem.appendChild(newsFooter);

        newsContainer.appendChild(newsItem);
    });
});