let allMovies = typeof allMovieData !== 'undefined' ? allMovieData : [];
let isLoading = allMovies.length === 0;

const contentArea = document.getElementById('content-area');
const tabs = document.querySelectorAll('.tab-item');
const movieModal = document.getElementById('movie-modal');
const modalBody = document.getElementById('modal-body');
const closeMovieBtn = document.getElementById('close-movie-btn');

function getRandomAvatar() {
    const id = Math.floor(Math.random() * 8) + 1;
    return `avatars/avatar${id}.jpg`;
}

// Close modal when clicking Back or outside
function closeFilmPage() {
    movieModal.classList.remove('active');
    setTimeout(() => {
        movieModal.style.display = "none";
    }, 300); // Wait for transition
}

closeMovieBtn.onclick = closeFilmPage;

window.onclick = (event) => {
    if (event.target == movieModal) closeFilmPage();
};

// No longer need loadMovies() fetch, data is loaded via <script> tag
function initialize() {
    if (allMovies.length > 0) {
        isLoading = false;
        renderHome();
    } else {
        contentArea.innerHTML = `<div class="loading-spinner">Error: Movie data not found.</div>`;
    }
}

function renderMovieCard(movie) {
    const posterUrl = movie.poster_url || 'https://via.placeholder.com/200x300?text=No+Poster';
    return `
        <div class="movie-card" onclick="showMovieDetails('${movie.id}')">
            <img src="${posterUrl}" alt="${movie.title}" loading="lazy">
        </div>
    `;
}

function showMovieDetails(id) {
    const movie = allMovies.find(m => m.id == id);
    if (!movie) return;

    const runtime = movie.runtime ? `${movie.runtime} min` : 'N/A';
    const trailerUrl = `https://www.youtube.com/results?search_query=${encodeURIComponent(movie.title + ' ' + movie.year + ' trailer')}`;

    modalBody.innerHTML = `
        <img src="${movie.poster_url}" class="modal-poster">
        <h2 class="modal-title">${movie.title}</h2>
        <div class="modal-meta">${movie.year} • ${runtime} • ★ ${movie.rating}</div>
        
        <div class="modal-actions">
            <button class="btn-trailer" onclick="window.open('${trailerUrl}', '_blank')">
                <i class="fa-solid fa-play"></i> Watch Trailer
            </button>
        </div>

        <div class="modal-section-title">Synopsis</div>
        <p class="modal-synopsis">${movie.overview || 'No synopsis available.'}</p>

        <div class="modal-info-grid">
            <div>
                <span class="info-label">Director</span>
                <span>${movie.director || 'N/A'}</span>
            </div>
            <div>
                <span class="info-label">Genres</span>
                <span>${movie.genres || 'N/A'}</span>
            </div>
        </div>

        <div class="modal-section-title">Cast</div>
        <div class="cast-scroller">
            ${movie.cast && movie.cast.length > 0 ? movie.cast.map(actor => `
                <div class="cast-member">
                    <img src="${actor.image_url || 'https://via.placeholder.com/60x60?text=?'}" class="cast-avatar" alt="${actor.name}">
                    <div class="cast-name">${actor.name}</div>
                </div>
            `).join('') : '<span>No cast information.</span>'}
        </div>

        <p style="color: var(--text-secondary); font-size: 0.7rem; margin-top: 20px; text-align: center;">
            TMDB ID: ${movie.id} • Popularity: ${Math.round(movie.popularity)}
        </p>
    `;
    movieModal.style.display = "block";
    // Trigger transition
    setTimeout(() => {
        movieModal.classList.add('active');
    }, 10);
}

let currentHomeTab = 'Films';
let currentActivityTab = 'Friends';

function renderHome() {
    if (isLoading) {
        contentArea.innerHTML = `<div class="loading-spinner">Loading movies...</div>`;
        return;
    }

    let html = `
        <div class="sub-tabs">
            <button class="sub-tab ${currentHomeTab === 'Films' ? 'active' : ''}" data-home-tab="Films">Films</button>
            <button class="sub-tab ${currentHomeTab === 'Reviews' ? 'active' : ''}" data-home-tab="Reviews">Reviews</button>
            <button class="sub-tab ${currentHomeTab === 'Lists' ? 'active' : ''}" data-home-tab="Lists">Lists</button>
            <button class="sub-tab ${currentHomeTab === 'Journal' ? 'active' : ''}" data-home-tab="Journal">Journal</button>
        </div>
        <div id="home-content">
            ${currentHomeTab === 'Films' ? renderHomeFilms() : 
             (currentHomeTab === 'Lists' ? renderHomeLists() : 
             (currentHomeTab === 'Journal' ? renderHomeJournal() : renderHomeReviews()))}
        </div>
    `;
    contentArea.innerHTML = html;

    // Add listeners to home tabs
    const homeTabs = document.querySelectorAll('.sub-tab[data-home-tab]');
    homeTabs.forEach(tab => {
        tab.addEventListener('click', (e) => {
            currentHomeTab = e.target.getAttribute('data-home-tab');
            renderHome();
        });
    });
}

function renderHomeFilms() {
    return `
        <div class="section-header">
            <h2>Popular this week</h2>
            <i class="fa-solid fa-chevron-right"></i>
        </div>
        <div class="movie-grid">
            ${allMovies.slice(0, 60).map(movie => renderMovieCard(movie)).join('')}
        </div>
    `;
}

function renderHomeReviews() {
    const obsessionMovie = allMovies.find(m => m.title === "Obsession") || allMovies[1];
    const reviews = [
        { user: "cinephile_99", rating: "★★★★★", text: "Absolutely haunting. The atmosphere Curry Barker creates is unmatched in modern horror. A masterpiece of suspense." },
        { user: "midnight_watcher", rating: "★★★★½", text: "The One Wish Willow is such a cool concept. Michael Johnston delivers a breakout performance. Don't skip this one!" },
        { user: "horror_junkie", rating: "★★★★", text: "Better than I expected. Genuinely scary in parts and the ending really sticks with you. Letterboxd needs more of this." },
        { user: "film_bro_88", rating: "★★★★★", text: "The cinematography is incredible. Every frame feels like a painting. Obsession is easily the best film of 2026 so far." },
        { user: "emma_v", rating: "★★★½", text: "Good but a bit slow in the middle. Still, the payoff is well worth the wait. Strong recommendation for horror fans." }
    ];

    let html = `
        <div class="section-header">
            <h2>Popular this week</h2>
            <i class="fa-solid fa-chevron-right"></i>
        </div>
        <div class="reviews-list">
    `;

    reviews.forEach(review => {
        html += `
            <div class="review-card">
                <div class="review-user-info">
                    <img src="${getRandomAvatar()}" class="avatar">
                    <span class="username">${review.user}</span>
                    <span class="review-rating">${review.rating}</span>
                </div>
                <div class="review-movie-info">
                    <img src="${obsessionMovie.poster_url}" class="review-poster">
                    <div class="review-text">${review.text}</div>
                </div>
            </div>
        `;
    });

    html += `</div>`;
    return html;
}

function renderHomeLists() {
    const lists = [
        {
            title: "2026 Oscar Predictions",
            author: "academy_insider",
            count: 24,
            movies: allMovies.slice(0, 5)
        },
        {
            title: "Haunting Atmosphere: The New Wave of Horror",
            author: "midnight_watcher",
            count: 15,
            movies: [allMovies.find(m => m.title === "Obsession") || allMovies[1], ...allMovies.slice(10, 14)]
        },
        {
            title: "Cinematography Masterclasses",
            author: "lens_crafter",
            count: 42,
            movies: allMovies.slice(20, 25)
        },
        {
            title: "Cannes 2026: The Highlights",
            author: "festival_junkie",
            count: 12,
            movies: allMovies.slice(30, 35)
        }
    ];

    let html = `
        <div class="section-header">
            <h2>Popular this week</h2>
            <i class="fa-solid fa-chevron-right"></i>
        </div>
        <div class="lists-container">
    `;

    lists.forEach(list => {
        html += `
            <div class="list-card">
                <div class="list-stacked-posters">
                    ${list.movies.map(movie => `
                        <img src="${movie.poster_url}" class="stacked-poster" alt="${movie.title}">
                    `).join('')}
                </div>
                <div class="list-details">
                    <h3>${list.title}</h3>
                    <div class="list-meta">
                        <img src="${getRandomAvatar()}" style="width: 16px; height: 16px; border-radius: 50%; object-fit: cover;">
                        <span>${list.author}</span>
                        <span>•</span>
                        <span>${list.count} films</span>
                    </div>
                </div>
            </div>
        `;
    });

    html += `</div>`;
    return html;
}

function renderHomeJournal() {
    const articles = [
        {
            tag: "Interview",
            title: "Curry Barker on the Dark Mythology of 'Obsession'",
            excerpt: "We sit down with the breakout director to discuss his viral horror hit and the secrets behind the One Wish Willow.",
            image: allMovies.find(m => m.title === "Obsession")?.poster_url || allMovies[1].poster_url
        },
        {
            tag: "News",
            title: "Cannes 2026: The Complete Winners List",
            excerpt: "From the Palme d'Or to the Un Certain Regard prize, see every film that took home an award at the Croisette.",
            image: allMovies[5].poster_url
        },
        {
            tag: "Feature",
            title: "Why 2026 is the Year of the Psychological Thriller",
            excerpt: "Exploring the cinematic trends that are keeping us on the edge of our seats this season.",
            image: allMovies[10].poster_url
        }
    ];

    let html = `
        <div class="section-header">
            <h2>Latest from the Journal</h2>
            <i class="fa-solid fa-chevron-right"></i>
        </div>
        <div class="journal-container">
    `;

    articles.forEach(article => {
        html += `
            <div class="journal-card">
                <img src="${article.image}" class="journal-hero">
                <div class="journal-body">
                    <span class="journal-tag">${article.tag}</span>
                    <h3 class="journal-title">${article.title}</h3>
                    <p class="journal-excerpt">${article.excerpt}</p>
                </div>
            </div>
        `;
    });

    html += `</div>`;
    return html;
}

function renderSearch() {
    contentArea.innerHTML = `
        <div class="search-container" style="margin-bottom: 20px;">
            <input type="text" id="movie-search" placeholder="Search 5,000+ movies..." 
                   style="width: 100%; padding: 12px; border-radius: 8px; border: none; background: #1b2228; color: white;">
        </div>
        <div id="search-results" class="movie-grid search-results-grid">
            <!-- Search results will appear here -->
        </div>
        <div id="genre-browse">
            <div class="section-header">
                <h2>Browse by Genre</h2>
            </div>
            <div class="genre-list" style="display: flex; flex-wrap: wrap; gap: 8px;">
                ${['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Thriller', 'Animation', 'Crime', 'Documentary', 'Fantasy', 'Mystery', 'Romance'].map(genre => `
                    <div class="genre-tag" onclick="renderGenrePage('${genre}')" 
                         style="background: #2c3440; padding: 10px 20px; border-radius: 20px; font-size: 0.8rem; cursor: pointer;">
                        ${genre}
                    </div>
                `).join('')}
            </div>
        </div>
    `;

    const searchInput = document.getElementById('movie-search');
    const searchResults = document.getElementById('search-results');
    const genreBrowse = document.getElementById('genre-browse');

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        if (query.length < 2) {
            searchResults.innerHTML = '';
            genreBrowse.style.display = 'block';
            return;
        }

        genreBrowse.style.display = 'none';
        const filtered = allMovies
            .filter(m => m.title.toLowerCase().includes(query))
            .slice(0, 30);

        searchResults.innerHTML = filtered.map(movie => renderMovieCard(movie)).join('');
    });
}

function renderGenrePage(genre) {
    const filtered = allMovies.filter(m => m.genres && m.genres.includes(genre)).slice(0, 60);
    
    contentArea.innerHTML = `
        <div class="genre-header" style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
            <button onclick="renderSearch()" style="background: none; border: none; color: var(--accent); cursor: pointer; font-size: 1.2rem;">
                <i class="fa-solid fa-chevron-left"></i>
            </button>
            <h2 style="font-size: 1rem; text-transform: uppercase; letter-spacing: 1px;">Top in ${genre}</h2>
        </div>
        <div class="movie-grid">
            ${filtered.map(movie => renderMovieCard(movie)).join('')}
        </div>
    `;
}

function renderActivity() {
    let html = `
        <h1 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 20px;">Activity</h1>
        <div class="sub-tabs">
            <button class="sub-tab ${currentActivityTab === 'Friends' ? 'active' : ''}" data-activity-tab="Friends">Friends</button>
            <button class="sub-tab ${currentActivityTab === 'You' ? 'active' : ''}" data-activity-tab="You">You</button>
            <button class="sub-tab ${currentActivityTab === 'Incoming' ? 'active' : ''}" data-activity-tab="Incoming">Incoming</button>
        </div>
        <div id="activity-content">
            ${currentActivityTab === 'Friends' ? renderFriendsActivity() : 
             (currentActivityTab === 'You' ? renderYouActivity() : renderIncomingActivity())}
        </div>
    `;
    contentArea.innerHTML = html;

    // Add listeners to activity tabs
    const activityTabs = document.querySelectorAll('.sub-tab[data-activity-tab]');
    activityTabs.forEach(tab => {
        tab.addEventListener('click', (e) => {
            currentActivityTab = e.target.getAttribute('data-activity-tab');
            renderActivity();
        });
    });
}

function renderFriendsActivity() {
    const mockActivity = [
        { user: "jack", action: "watched", movie: "Obsession", rating: "★★★★★", time: "2h ago" },
        { user: "emma", action: "liked", movie: "The Batman", rating: "★★★★½", time: "4h ago" },
        { user: "alex", action: "reviewed", movie: "Inception", rating: "★★★★", time: "1d ago" },
        { user: "sarah", action: "watched", movie: "Interstellar", rating: "★★★★★", time: "1d ago" }
    ];

    let html = `<div class="activity-list">`;
    mockActivity.forEach(item => {
        const movie = allMovies.find(m => m.title === item.movie) || allMovies[0];
        const posterUrl = movie.poster_url || 'https://via.placeholder.com/60x90?text=No+Poster';
        
        html += `
            <div class="activity-item">
                <div class="activity-header">
                    <img src="${getRandomAvatar()}" class="avatar" style="width: 32px; height: 32px; border-radius: 50%; object-fit: cover;">
                    <div class="activity-info">
                        <span class="username">${item.user}</span> 
                        <span class="action-text">${item.action}</span>
                        <div style="color: var(--text-secondary); font-size: 0.7rem;">${item.time}</div>
                    </div>
                </div>
                <div class="activity-content">
                    <img src="${posterUrl}" class="mini-poster" onclick="showMovieDetails('${movie.id}')">
                    <div class="activity-details">
                        <div class="movie-title">${item.movie}</div>
                        <div class="rating">${item.rating}</div>
                    </div>
                </div>
            </div>
        `;
    });
    html += `</div>`;
    return html;
}

function renderYouActivity() {
    return `
        <div style="text-align: center; padding: 40px 20px; color: var(--text-secondary);">
            <i class="fa-solid fa-user-clock" style="font-size: 3rem; margin-bottom: 20px; opacity: 0.3;"></i>
            <p>Your recent activity will appear here.</p>
        </div>
    `;
}

function renderIncomingActivity() {
    return `
        <div style="text-align: center; padding: 40px 20px; color: var(--text-secondary);">
            <i class="fa-solid fa-bell" style="font-size: 3rem; margin-bottom: 20px; opacity: 0.3;"></i>
            <p>No new notifications or mentions.</p>
        </div>
    `;
}

function renderProfile() {
    contentArea.innerHTML = `
        <div class="profile-header" style="text-align: center; padding: 20px 0;">
            <img src="avatars/avatar3.jpg" style="width: 80px; height: 80px; margin: 0 auto 10px; border-radius: 50%; object-fit: cover;">
            <h2 style="font-size: 1.2rem;">Movie Buff</h2>
            <p style="color: var(--text-secondary); font-size: 0.9rem;">London, UK</p>
        </div>
        <div class="profile-stats" style="display: flex; justify-content: space-around; padding: 20px 0; border-top: 1px solid var(--border-color);">
            <div style="text-align: center;"><div style="font-weight: 700;">452</div><div style="font-size: 0.7rem; color: var(--text-secondary);">FILMS</div></div>
            <div style="text-align: center;"><div style="font-weight: 700;">12</div><div style="font-size: 0.7rem; color: var(--text-secondary);">LISTS</div></div>
            <div style="text-align: center;"><div style="font-weight: 700;">89</div><div style="font-size: 0.7rem; color: var(--text-secondary);">FOLLOWING</div></div>
            <div style="text-align: center;"><div style="font-weight: 700;">154</div><div style="font-size: 0.7rem; color: var(--text-secondary);">FOLLOWERS</div></div>
        </div>
        <div class="section-header">
            <h2>Recent Watchlist</h2>
        </div>
        <div class="movie-grid">
            ${allMovies.slice(100, 103).map(movie => renderMovieCard(movie)).join('')}
        </div>
    `;
}

function handleTabClick(e) {
    const tab = e.currentTarget;
    const tabName = tab.getAttribute('data-tab');
    
    tabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    
    // Toggle nav bar visibility - only show on home
    const navBar = document.querySelector('.ios-nav-bar');
    if (tabName === 'home') {
        navBar.style.display = 'flex';
    } else {
        navBar.style.display = 'none';
    }
    
    switch(tabName) {
        case 'home': renderHome(); break;
        case 'search': renderSearch(); break;
        case 'activity': renderActivity(); break;
        case 'profile': renderProfile(); break;
    }
}

tabs.forEach(tab => tab.addEventListener('click', handleTabClick));

// Initial Load
initialize();
