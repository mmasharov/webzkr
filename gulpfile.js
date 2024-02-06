import gulp from 'gulp';
import browsersync from 'browser-sync';
import dartSass from 'sass';
import gulpSass from 'gulp-sass';
import rename from 'gulp-rename';
import autoprefixer from 'gulp-autoprefixer';
import cleancss from 'gulp-clean-css';
import webpack from 'webpack-stream';

const sass = gulpSass(dartSass);

gulp.task('server', () => {
    browsersync.init({
        server: './',
        port: 4000,
        notify: true
    });

    gulp.watch('*.html').on('change', browsersync.reload);
});

gulp.task('styles', () => {
    return gulp.src('sass/**/*.+(scss|sass)')
        .pipe(sass({outputStyle: 'compressed'})).on('error', sass.logError)
        .pipe(rename({suffix: '.min', prefix: ''}))
        .pipe(autoprefixer())
        .pipe(cleancss({compatibility: 'ie8'}))
        .pipe(gulp.dest('./'))
        .pipe(browsersync.stream());
});

gulp.task('build-js', () => {
    return gulp.src('./js/main.js')
        .pipe(webpack({
            mode: "development",
            output: {
                filename: "script.js"
            },
            watch: false,
            devtool: "source-map",
            module: {
                rules: [
                    {
                        test: /\.m?js$/,
                        exclude: /(node_modules|bower_components)/,
                        use: {
                            loader: "babel-loader",
                            options: {
                                presets: [['@babel/preset-env', {
                                    debug: true,
                                    corejs: 3,
                                    useBuiltIns: 'usage'
                                }]]
                            }
                        }
                    }
                ]
            }
        }))
        .pipe(gulp.dest('./'))
        .on('end', browsersync.reload);
});

gulp.task('watch', () => {
    gulp.watch('*.html').on('change', browsersync.reload);
    gulp.watch('sass/**/*.+(scss|sass|css)', gulp.parallel('styles'));
    gulp.watch('./js/**/*.js', gulp.parallel('build-js'));
});

gulp.task('default', gulp.parallel('server', 'watch', 'styles', 'build-js'));