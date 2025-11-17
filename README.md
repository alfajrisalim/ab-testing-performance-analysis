# ab-testing-performance-analysis
Sebuah proyek simulasi yang fokus pada penerapan SQL dan Python untuk menganalisis hasil eksperimen A/B Testing produk digital, dengan tujuan mengukur dampak Treatment Group (B) terhadap Control Group (A) pada metrik kunci engagement.

🎯 Tujuan Teknis Proyek
Proyek ini bertujuan untuk mendemonstrasikan kemampuan Data Science dalam aspek-aspek berikut:

SQL for Metric Definition: Menggunakan SQL untuk mendefinisikan dan menghitung metrik bisnis (KPI) dari data event mentah, khususnya Click-Through Rate (CTR).

Data Structure & Querying: Menerapkan query SQL intermediate seperti JOIN untuk menghubungkan tabel users dan events, serta menggunakan SUM dengan CASE statements (conditional aggregation) untuk perhitungan metrik per grup.

Data Simulation: Mampu membuat dataset simulasi menggunakan Python (Pandas & NumPy) untuk mereplikasi struktur data database yang kompleks.

Data Storytelling: Menganalisis hasil numerik dan menarik kesimpulan bisnis yang terukur.

⚙️ Metodologi
Simulasi Data: Menggunakan Python, 10.000 data pengguna dan 50.000 data event (view/click) disimulasikan dan disimpan ke dalam database SQLite (ab_testing.db).

Penyiapan Database: Data di-load ke dalam dua tabel: users dan events.

Eksekusi Query: Query SQL yang kompleks dijalankan melalui DBeaver untuk menghitung total_views, total_clicks, dan click_through_rate_pct secara terpisah untuk setiap grup.

      SELECT
          T1.test_group,
          SUM(CASE WHEN T2.event_type = 'view' THEN 1 ELSE 0 END) AS total_views,
          SUM(CASE WHEN T2.event_type = 'click' THEN 1 ELSE 0 END) AS total_clicks,
          (SUM(CASE WHEN T2.event_type = 'click' THEN 1 ELSE 0 END) * 1.0) /
           SUM(CASE WHEN T2.event_type = 'view' THEN 1 ELSE 0 END) * 100 AS click_through_rate_pct
      FROM
          users AS T1
      JOIN
          events AS T2 ON T1.user_id = T2.user_id
      GROUP BY
          T1.test_group;
test_group     |  total_views | total_clicks |  click_through_rate_pct
A (Control)    | 21367        | 3821         |  17.88%
B (Eksperimen) | 19811        | 5001         |  25.24%

Kesimpulan
Peningkatan Engagement: Berdasarkan analisis SQL, Grup Eksperimen (B) menunjukkan CTR sebesar 25.24%, yang merupakan peningkatan signifikan sebesar 7.36 percentage points dari Grup Kontrol (A).

Rekomendasi: Perubahan atau fitur yang diuji pada Grup B harus diimplementasikan secara penuh (rollout) karena terbukti secara substansial meningkatkan metrik engagement pengguna.


