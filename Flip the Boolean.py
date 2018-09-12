<!DOCTYPE html>
<!-- saved from url=(0046)https://edabit.com/challenge/NLY7zGMYocsTbeS6n -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <link rel="stylesheet" type="text/css" class="__meteor-css__" href="./Flip the Boolean_files/0405c384528de563239290d4ceb9a7a63107aae2.css">
  <link rel="stylesheet" type="text/css" class="__meteor-css__" href="./Flip the Boolean_files/80b65bddb41322d95880e7f008b1b2bd5019d6e7.css">
<meta name="fragment" content="!">

<script type="text/javascript" async="" src="./Flip the Boolean_files/analytics.js.download"></script><script async="" src="./Flip the Boolean_files/hotjar-399651.js.download"></script><style type="text/css">/* Common, default styles for the notification box */

.s-alert-box,
.s-alert-box * {
    box-sizing: border-box;
}

.s-alert-box {
    position: fixed;
    background: rgba(42,45,50,0.85);
    padding: 22px;
    line-height: 1.4;
    z-index: 1000;
    pointer-events: none;
    color: rgba(250,251,255,0.95);
    font-size: 100%;
    font-family: 'Helvetica Neue', 'Segoe UI', Helvetica, Arial, sans-serif;
    max-width: 300px;
    -webkit-transition: top .4s, bottom .4s;
    transition: top .4s, bottom .4s;
}

.s-alert-box.s-alert-show {
    pointer-events: auto;
}

.s-alert-box a {
    color: inherit;
    opacity: 0.7;
    font-weight: 700;
}

.s-alert-box a:hover,
.s-alert-box a:focus {
    opacity: 1;
}

.s-alert-box p {
    margin: 0;
}

.s-alert-box.s-alert-show,
.s-alert-box.s-alert-visible {
    pointer-events: auto;
}

/* positions */

.s-alert-bottom-left {
    top: auto;
    right: auto;
    bottom: 30px;
    left: 30px;
}
.s-alert-top-left {
    top: 30px;
    right: auto;
    bottom: auto;
    left: 30px;
}
.s-alert-top-right {
    top: 30px;
    right: 30px;
    bottom: auto;
    left: auto;
}
.s-alert-bottom-right { /*default*/
    top: auto;
    right: 30px;
    bottom: 30px;
    left: auto;
}
.s-alert-bottom {
    width: 100%;
    max-width: 100%;
    bottom: 0;
    left: 0;
    right: 0;
    top: auto;
}
.s-alert-top {
    width: 100%;
    max-width: 100%;
    top: 0;
    left: 0;
    right: 0;
    bottom: auto;
}

/* conditions */

.s-alert-info {
    background: #2987CD;
    color: #fff;
}
.s-alert-success {
    background: #2DB84B;
    color: #fff;
}
.s-alert-warning {
    background: #FABC2E;
    color: #fff;
}
.s-alert-error {
    background: #DB2828;
    color: #fff;
}

[class^="s-alert-effect-"].s-alert-hide,
[class*=" s-alert-effect-"].s-alert-hide {
    -webkit-animation-direction: reverse;
    animation-direction: reverse;
}

/* height measurement helper */
.s-alert-box-height {
    visibility: hidden;
    position: fixed;
}
</style><style type="text/css">/* Jelly */

.s-alert-effect-jelly a {
    color: #fff;
}

.s-alert-effect-jelly a:hover,
.s-alert-effect-jelly a:focus {
    color: #fff;
}

.s-alert-effect-jelly .s-alert-close::before,
.s-alert-effect-jelly .s-alert-close::after {
    background: #fff;
}

.s-alert-effect-jelly .s-alert-close:hover::before,
.s-alert-effect-jelly .s-alert-close:hover::after {
    background: #fff;
}

.s-alert-effect-jelly.s-alert-show {
    -webkit-animation-name: animJelly;
    animation-name: animJelly;
    -webkit-animation-duration: 1s;
    animation-duration: 1s;
    -webkit-animation-timing-function: linear;
    animation-timing-function: linear;
}

.s-alert-effect-jelly.s-alert-hide {
    -webkit-animation-name: animFade;
    animation-name: animFade;
    -webkit-animation-duration: 0.3s;
    animation-duration: 0.3s;
}

@-webkit-keyframes animFade {
    0% { opacity: 0; }
    100% { opacity: 1; }
}

@keyframes animFade {
    0% { opacity: 0; }
    100% { opacity: 1; }
}

/* Generated with Bounce.js. Edit at http://goo.gl/6iLZu5 */

@-webkit-keyframes animJelly {
    0% { -webkit-transform: matrix3d(0.7, 0, 0, 0, 0, 0.7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.7, 0, 0, 0, 0, 0.7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    2.083333% { -webkit-transform: matrix3d(0.75266, 0, 0, 0, 0, 0.76342, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.75266, 0, 0, 0, 0, 0.76342, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    4.166667% { -webkit-transform: matrix3d(0.81071, 0, 0, 0, 0, 0.84545, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.81071, 0, 0, 0, 0, 0.84545, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    6.25% { -webkit-transform: matrix3d(0.86808, 0, 0, 0, 0, 0.9286, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.86808, 0, 0, 0, 0, 0.9286, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    8.333333% { -webkit-transform: matrix3d(0.92038, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.92038, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    10.416667% { -webkit-transform: matrix3d(0.96482, 0, 0, 0, 0, 1.05202, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.96482, 0, 0, 0, 0, 1.05202, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    12.5% { -webkit-transform: matrix3d(1, 0, 0, 0, 0, 1.08204, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1, 0, 0, 0, 0, 1.08204, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    14.583333% { -webkit-transform: matrix3d(1.02563, 0, 0, 0, 0, 1.09149, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.02563, 0, 0, 0, 0, 1.09149, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    16.666667% { -webkit-transform: matrix3d(1.04227, 0, 0, 0, 0, 1.08453, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.04227, 0, 0, 0, 0, 1.08453, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    18.75% { -webkit-transform: matrix3d(1.05102, 0, 0, 0, 0, 1.06666, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.05102, 0, 0, 0, 0, 1.06666, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    20.833333% { -webkit-transform: matrix3d(1.05334, 0, 0, 0, 0, 1.04355, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.05334, 0, 0, 0, 0, 1.04355, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    22.916667% { -webkit-transform: matrix3d(1.05078, 0, 0, 0, 0, 1.02012, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.05078, 0, 0, 0, 0, 1.02012, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    25% { -webkit-transform: matrix3d(1.04487, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.04487, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    27.083333% { -webkit-transform: matrix3d(1.03699, 0, 0, 0, 0, 0.98534, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.03699, 0, 0, 0, 0, 0.98534, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    29.166667% { -webkit-transform: matrix3d(1.02831, 0, 0, 0, 0, 0.97688, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.02831, 0, 0, 0, 0, 0.97688, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    31.25% { -webkit-transform: matrix3d(1.01973, 0, 0, 0, 0, 0.97422, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.01973, 0, 0, 0, 0, 0.97422, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    33.333333% { -webkit-transform: matrix3d(1.01191, 0, 0, 0, 0, 0.97618, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.01191, 0, 0, 0, 0, 0.97618, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    35.416667% { -webkit-transform: matrix3d(1.00526, 0, 0, 0, 0, 0.98122, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00526, 0, 0, 0, 0, 0.98122, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    37.5% { -webkit-transform: matrix3d(1, 0, 0, 0, 0, 0.98773, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1, 0, 0, 0, 0, 0.98773, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    39.583333% { -webkit-transform: matrix3d(0.99617, 0, 0, 0, 0, 0.99433, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99617, 0, 0, 0, 0, 0.99433, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    41.666667% { -webkit-transform: matrix3d(0.99368, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99368, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    43.75% { -webkit-transform: matrix3d(0.99237, 0, 0, 0, 0, 1.00413, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99237, 0, 0, 0, 0, 1.00413, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    45.833333% { -webkit-transform: matrix3d(0.99202, 0, 0, 0, 0, 1.00651, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99202, 0, 0, 0, 0, 1.00651, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    47.916667% { -webkit-transform: matrix3d(0.99241, 0, 0, 0, 0, 1.00726, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99241, 0, 0, 0, 0, 1.00726, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    50% { -webkit-transform: matrix3d(0.99329, 0, 0, 0, 0, 1.00671, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99329, 0, 0, 0, 0, 1.00671, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    52.083333% { -webkit-transform: matrix3d(0.99447, 0, 0, 0, 0, 1.00529, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99447, 0, 0, 0, 0, 1.00529, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    54.166667% { -webkit-transform: matrix3d(0.99577, 0, 0, 0, 0, 1.00346, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99577, 0, 0, 0, 0, 1.00346, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    56.25% { -webkit-transform: matrix3d(0.99705, 0, 0, 0, 0, 1.0016, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99705, 0, 0, 0, 0, 1.0016, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    58.333333% { -webkit-transform: matrix3d(0.99822, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99822, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    60.416667% { -webkit-transform: matrix3d(0.99921, 0, 0, 0, 0, 0.99884, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99921, 0, 0, 0, 0, 0.99884, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    62.5% { -webkit-transform: matrix3d(1, 0, 0, 0, 0, 0.99816, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1, 0, 0, 0, 0, 0.99816, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    64.583333% { -webkit-transform: matrix3d(1.00057, 0, 0, 0, 0, 0.99795, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00057, 0, 0, 0, 0, 0.99795, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    66.666667% { -webkit-transform: matrix3d(1.00095, 0, 0, 0, 0, 0.99811, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00095, 0, 0, 0, 0, 0.99811, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    68.75% { -webkit-transform: matrix3d(1.00114, 0, 0, 0, 0, 0.99851, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00114, 0, 0, 0, 0, 0.99851, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    70.833333% { -webkit-transform: matrix3d(1.00119, 0, 0, 0, 0, 0.99903, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00119, 0, 0, 0, 0, 0.99903, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    72.916667% { -webkit-transform: matrix3d(1.00114, 0, 0, 0, 0, 0.99955, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00114, 0, 0, 0, 0, 0.99955, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    75% { -webkit-transform: matrix3d(1.001, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.001, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    77.083333% { -webkit-transform: matrix3d(1.00083, 0, 0, 0, 0, 1.00033, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00083, 0, 0, 0, 0, 1.00033, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    79.166667% { -webkit-transform: matrix3d(1.00063, 0, 0, 0, 0, 1.00052, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00063, 0, 0, 0, 0, 1.00052, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    81.25% { -webkit-transform: matrix3d(1.00044, 0, 0, 0, 0, 1.00058, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00044, 0, 0, 0, 0, 1.00058, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    83.333333% { -webkit-transform: matrix3d(1.00027, 0, 0, 0, 0, 1.00053, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00027, 0, 0, 0, 0, 1.00053, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    85.416667% { -webkit-transform: matrix3d(1.00012, 0, 0, 0, 0, 1.00042, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00012, 0, 0, 0, 0, 1.00042, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    87.5% { -webkit-transform: matrix3d(1, 0, 0, 0, 0, 1.00027, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1, 0, 0, 0, 0, 1.00027, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    89.583333% { -webkit-transform: matrix3d(0.99991, 0, 0, 0, 0, 1.00013, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99991, 0, 0, 0, 0, 1.00013, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    91.666667% { -webkit-transform: matrix3d(0.99986, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99986, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    93.75% { -webkit-transform: matrix3d(0.99983, 0, 0, 0, 0, 0.99991, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99983, 0, 0, 0, 0, 0.99991, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    95.833333% { -webkit-transform: matrix3d(0.99982, 0, 0, 0, 0, 0.99985, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99982, 0, 0, 0, 0, 0.99985, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    97.916667% { -webkit-transform: matrix3d(0.99983, 0, 0, 0, 0, 0.99984, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99983, 0, 0, 0, 0, 0.99984, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    100% { -webkit-transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
}

@keyframes animJelly {
    0% { -webkit-transform: matrix3d(0.7, 0, 0, 0, 0, 0.7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.7, 0, 0, 0, 0, 0.7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    2.083333% { -webkit-transform: matrix3d(0.75266, 0, 0, 0, 0, 0.76342, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.75266, 0, 0, 0, 0, 0.76342, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    4.166667% { -webkit-transform: matrix3d(0.81071, 0, 0, 0, 0, 0.84545, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.81071, 0, 0, 0, 0, 0.84545, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    6.25% { -webkit-transform: matrix3d(0.86808, 0, 0, 0, 0, 0.9286, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.86808, 0, 0, 0, 0, 0.9286, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    8.333333% { -webkit-transform: matrix3d(0.92038, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.92038, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    10.416667% { -webkit-transform: matrix3d(0.96482, 0, 0, 0, 0, 1.05202, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.96482, 0, 0, 0, 0, 1.05202, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    12.5% { -webkit-transform: matrix3d(1, 0, 0, 0, 0, 1.08204, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1, 0, 0, 0, 0, 1.08204, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    14.583333% { -webkit-transform: matrix3d(1.02563, 0, 0, 0, 0, 1.09149, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.02563, 0, 0, 0, 0, 1.09149, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    16.666667% { -webkit-transform: matrix3d(1.04227, 0, 0, 0, 0, 1.08453, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.04227, 0, 0, 0, 0, 1.08453, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    18.75% { -webkit-transform: matrix3d(1.05102, 0, 0, 0, 0, 1.06666, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.05102, 0, 0, 0, 0, 1.06666, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    20.833333% { -webkit-transform: matrix3d(1.05334, 0, 0, 0, 0, 1.04355, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.05334, 0, 0, 0, 0, 1.04355, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    22.916667% { -webkit-transform: matrix3d(1.05078, 0, 0, 0, 0, 1.02012, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.05078, 0, 0, 0, 0, 1.02012, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    25% { -webkit-transform: matrix3d(1.04487, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.04487, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    27.083333% { -webkit-transform: matrix3d(1.03699, 0, 0, 0, 0, 0.98534, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.03699, 0, 0, 0, 0, 0.98534, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    29.166667% { -webkit-transform: matrix3d(1.02831, 0, 0, 0, 0, 0.97688, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.02831, 0, 0, 0, 0, 0.97688, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    31.25% { -webkit-transform: matrix3d(1.01973, 0, 0, 0, 0, 0.97422, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.01973, 0, 0, 0, 0, 0.97422, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    33.333333% { -webkit-transform: matrix3d(1.01191, 0, 0, 0, 0, 0.97618, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.01191, 0, 0, 0, 0, 0.97618, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    35.416667% { -webkit-transform: matrix3d(1.00526, 0, 0, 0, 0, 0.98122, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00526, 0, 0, 0, 0, 0.98122, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    37.5% { -webkit-transform: matrix3d(1, 0, 0, 0, 0, 0.98773, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1, 0, 0, 0, 0, 0.98773, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    39.583333% { -webkit-transform: matrix3d(0.99617, 0, 0, 0, 0, 0.99433, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99617, 0, 0, 0, 0, 0.99433, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    41.666667% { -webkit-transform: matrix3d(0.99368, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99368, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    43.75% { -webkit-transform: matrix3d(0.99237, 0, 0, 0, 0, 1.00413, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99237, 0, 0, 0, 0, 1.00413, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    45.833333% { -webkit-transform: matrix3d(0.99202, 0, 0, 0, 0, 1.00651, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99202, 0, 0, 0, 0, 1.00651, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    47.916667% { -webkit-transform: matrix3d(0.99241, 0, 0, 0, 0, 1.00726, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99241, 0, 0, 0, 0, 1.00726, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    50% { -webkit-transform: matrix3d(0.99329, 0, 0, 0, 0, 1.00671, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99329, 0, 0, 0, 0, 1.00671, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    52.083333% { -webkit-transform: matrix3d(0.99447, 0, 0, 0, 0, 1.00529, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99447, 0, 0, 0, 0, 1.00529, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    54.166667% { -webkit-transform: matrix3d(0.99577, 0, 0, 0, 0, 1.00346, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99577, 0, 0, 0, 0, 1.00346, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    56.25% { -webkit-transform: matrix3d(0.99705, 0, 0, 0, 0, 1.0016, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99705, 0, 0, 0, 0, 1.0016, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    58.333333% { -webkit-transform: matrix3d(0.99822, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99822, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    60.416667% { -webkit-transform: matrix3d(0.99921, 0, 0, 0, 0, 0.99884, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99921, 0, 0, 0, 0, 0.99884, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    62.5% { -webkit-transform: matrix3d(1, 0, 0, 0, 0, 0.99816, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1, 0, 0, 0, 0, 0.99816, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    64.583333% { -webkit-transform: matrix3d(1.00057, 0, 0, 0, 0, 0.99795, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00057, 0, 0, 0, 0, 0.99795, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    66.666667% { -webkit-transform: matrix3d(1.00095, 0, 0, 0, 0, 0.99811, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00095, 0, 0, 0, 0, 0.99811, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    68.75% { -webkit-transform: matrix3d(1.00114, 0, 0, 0, 0, 0.99851, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00114, 0, 0, 0, 0, 0.99851, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    70.833333% { -webkit-transform: matrix3d(1.00119, 0, 0, 0, 0, 0.99903, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00119, 0, 0, 0, 0, 0.99903, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    72.916667% { -webkit-transform: matrix3d(1.00114, 0, 0, 0, 0, 0.99955, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00114, 0, 0, 0, 0, 0.99955, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    75% { -webkit-transform: matrix3d(1.001, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.001, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    77.083333% { -webkit-transform: matrix3d(1.00083, 0, 0, 0, 0, 1.00033, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00083, 0, 0, 0, 0, 1.00033, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    79.166667% { -webkit-transform: matrix3d(1.00063, 0, 0, 0, 0, 1.00052, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00063, 0, 0, 0, 0, 1.00052, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    81.25% { -webkit-transform: matrix3d(1.00044, 0, 0, 0, 0, 1.00058, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00044, 0, 0, 0, 0, 1.00058, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    83.333333% { -webkit-transform: matrix3d(1.00027, 0, 0, 0, 0, 1.00053, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00027, 0, 0, 0, 0, 1.00053, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    85.416667% { -webkit-transform: matrix3d(1.00012, 0, 0, 0, 0, 1.00042, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1.00012, 0, 0, 0, 0, 1.00042, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    87.5% { -webkit-transform: matrix3d(1, 0, 0, 0, 0, 1.00027, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1, 0, 0, 0, 0, 1.00027, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    89.583333% { -webkit-transform: matrix3d(0.99991, 0, 0, 0, 0, 1.00013, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99991, 0, 0, 0, 0, 1.00013, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    91.666667% { -webkit-transform: matrix3d(0.99986, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99986, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    93.75% { -webkit-transform: matrix3d(0.99983, 0, 0, 0, 0, 0.99991, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99983, 0, 0, 0, 0, 0.99991, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    95.833333% { -webkit-transform: matrix3d(0.99982, 0, 0, 0, 0, 0.99985, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99982, 0, 0, 0, 0, 0.99985, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    97.916667% { -webkit-transform: matrix3d(0.99983, 0, 0, 0, 0, 0.99984, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(0.99983, 0, 0, 0, 0, 0.99984, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
    100% { -webkit-transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1); }
}</style><style type="text/css">.CodeMirror-fullscreen {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  height: auto;
  z-index: 9;
}
</style><script async="" src="./Flip the Boolean_files/modules-05aa331237e6102bd10203cd0b1b5287.js.download"></script><style type="text/css">iframe#_hjRemoteVarsFrame {display: none !important; width: 1px !important; height: 1px !important; opacity: 0 !important; pointer-events: none !important;}</style><title>Flip the Boolean - Python | Edabit</title><meta name="description" content="We&#39;re like Duolingo for learning to code. Earn points for correct solutions, unlock achievements and level up. Our coding challenges make learning to code fun and easy." dochead="1"><link rel="icon" type="image/png" href="https://s3.amazonaws.com/edabit-images/logo_main_medium.png" dochead="1"><meta name="keywords" content="coding challenges, programming challenges" dochead="1"><meta name="twitter:card" content="summary_large_image" dochead="1"><meta name="twitter:site" content="@edabit" dochead="1"><meta property="og:description" content="Edabit is like Duolingo for learning to code. Earn points for correct solutions, unlock achievements and level up. Our coding challenges make learning to code fun and easy." dochead="1"><meta property="og:image" content="https://s3.amazonaws.com/edabit-images/logo_wide_large.png" dochead="1"><meta property="og:site_name" content="edabit" dochead="1"><meta property="og:title" content="Explore 600+ FREE Coding Challenges | Edabit" dochead="1"><meta property="og:type" content="website" dochead="1"><script type="text/javascript" src="./Flip the Boolean_files/en"></script><link rel="icon" type="image/png" href="https://s3.amazonaws.com/edabit-images/logo_main_medium.png" dochead="1"><meta name="twitter:card" content="summary_large_image" dochead="1"><meta name="twitter:site" content="@edabit" dochead="1"><meta property="og:image" content="https://s3.amazonaws.com/edabit-images/logo_wide_large.png" dochead="1"><meta property="og:site_name" content="edabit" dochead="1"><meta property="og:type" content="website" dochead="1"><meta name="description" content="undefined" dochead="1"><meta name="keywords" content="undefined" dochead="1"><meta property="og:description" content="undefined" dochead="1"><meta property="og:title" content="undefined" dochead="1"><meta name="description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta property="og:title" content="Month Name" dochead="1"><meta name="description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta property="og:title" content="Month Name" dochead="1"><meta name="description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta property="og:title" content="Month Name" dochead="1"><meta name="description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta property="og:title" content="Month Name" dochead="1"><meta name="description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta property="og:title" content="Month Name" dochead="1"><meta name="description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta property="og:title" content="Month Name" dochead="1"><meta name="description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta property="og:title" content="Month Name" dochead="1"><meta name="description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Write a function. It will return the name of a month of the year, given the month number, according to the table below. Make sure you do not put any input or output statements in the function; the month number will be passed in and the string containing the name will be returned.

#Number	Month
-1	January
-2	February
-3	March
-4	April
-5	May
-6	June
-7	July
-8" dochead="1"><meta property="og:title" content="Month Name" dochead="1"><meta name="description" content="Create a function that takes two numbers as arguments and return their sum.

Examples
3, 2 ➞ 5

-3, -6 ➞ -9

7, 3 ➞ 10

Notes
Don&#39;t forget to return the result.
All tests contain valid numbers.
If you get stuck on a challenge, find help in the Resources tab.
If you&#39;re really stuck, unlock solutions in the Solutions tab." dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Create a function that takes two numbers as arguments and return their sum.

Examples
3, 2 ➞ 5

-3, -6 ➞ -9

7, 3 ➞ 10

Notes
Don&#39;t forget to return the result.
All tests contain valid numbers.
If you get stuck on a challenge, find help in the Resources tab.
If you&#39;re really stuck, unlock solutions in the Solutions tab." dochead="1"><meta property="og:title" content="Return the Sum of Two Numbers" dochead="1"><meta name="description" content="Create a function that takes two numbers as arguments and return their sum.

Examples
3, 2 ➞ 5

-3, -6 ➞ -9

7, 3 ➞ 10

Notes
Don&#39;t forget to return the result.
All tests contain valid numbers.
If you get stuck on a challenge, find help in the Resources tab.
If you&#39;re really stuck, unlock solutions in the Solutions tab." dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Create a function that takes two numbers as arguments and return their sum.

Examples
3, 2 ➞ 5

-3, -6 ➞ -9

7, 3 ➞ 10

Notes
Don&#39;t forget to return the result.
All tests contain valid numbers.
If you get stuck on a challenge, find help in the Resources tab.
If you&#39;re really stuck, unlock solutions in the Solutions tab." dochead="1"><meta property="og:title" content="Return the Sum of Two Numbers" dochead="1"><meta name="description" content="Create a function that takes two numbers as arguments and return their sum.

Examples
3, 2 ➞ 5

-3, -6 ➞ -9

7, 3 ➞ 10

Notes
Don&#39;t forget to return the result.
All tests contain valid numbers.
If you get stuck on a challenge, find help in the Resources tab.
If you&#39;re really stuck, unlock solutions in the Solutions tab." dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Create a function that takes two numbers as arguments and return their sum.

Examples
3, 2 ➞ 5

-3, -6 ➞ -9

7, 3 ➞ 10

Notes
Don&#39;t forget to return the result.
All tests contain valid numbers.
If you get stuck on a challenge, find help in the Resources tab.
If you&#39;re really stuck, unlock solutions in the Solutions tab." dochead="1"><meta property="og:title" content="Return the Sum of Two Numbers" dochead="1"><meta name="description" content="Create a function that takes two numbers as arguments and return their sum.

Examples
3, 2 ➞ 5

-3, -6 ➞ -9

7, 3 ➞ 10

Notes
Don&#39;t forget to return the result.
All tests contain valid numbers.
If you get stuck on a challenge, find help in the Resources tab.
If you&#39;re really stuck, unlock solutions in the Solutions tab." dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Create a function that takes two numbers as arguments and return their sum.

Examples
3, 2 ➞ 5

-3, -6 ➞ -9

7, 3 ➞ 10

Notes
Don&#39;t forget to return the result.
All tests contain valid numbers.
If you get stuck on a challenge, find help in the Resources tab.
If you&#39;re really stuck, unlock solutions in the Solutions tab." dochead="1"><meta property="og:title" content="Return the Sum of Two Numbers" dochead="1"><meta name="description" content="Create a function that takes two numbers as arguments and return their sum.

Examples
3, 2 ➞ 5

-3, -6 ➞ -9

7, 3 ➞ 10

Notes
Don&#39;t forget to return the result.
All tests contain valid numbers.
If you get stuck on a challenge, find help in the Resources tab.
If you&#39;re really stuck, unlock solutions in the Solutions tab." dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Create a function that takes two numbers as arguments and return their sum.

Examples
3, 2 ➞ 5

-3, -6 ➞ -9

7, 3 ➞ 10

Notes
Don&#39;t forget to return the result.
All tests contain valid numbers.
If you get stuck on a challenge, find help in the Resources tab.
If you&#39;re really stuck, unlock solutions in the Solutions tab." dochead="1"><meta property="og:title" content="Return the Sum of Two Numbers" dochead="1"><meta name="description" content="Create a function that takes two numbers as arguments and return their sum.

Examples
3, 2 ➞ 5

-3, -6 ➞ -9

7, 3 ➞ 10

Notes
Don&#39;t forget to return the result.
All tests contain valid numbers.
If you get stuck on a challenge, find help in the Resources tab.
If you&#39;re really stuck, unlock solutions in the Solutions tab." dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Create a function that takes two numbers as arguments and return their sum.

Examples
3, 2 ➞ 5

-3, -6 ➞ -9

7, 3 ➞ 10

Notes
Don&#39;t forget to return the result.
All tests contain valid numbers.
If you get stuck on a challenge, find help in the Resources tab.
If you&#39;re really stuck, unlock solutions in the Solutions tab." dochead="1"><meta property="og:title" content="Return the Sum of Two Numbers" dochead="1"><meta name="description" content="We&#39;re like Duolingo for learning to code. Earn points for correct solutions, unlock achievements and level up. Our coding challenges make learning to code fun and easy." dochead="1"><link rel="icon" type="image/png" href="https://s3.amazonaws.com/edabit-images/logo_main_medium.png" dochead="1"><meta name="keywords" content="coding challenges, programming challenges" dochead="1"><meta name="twitter:card" content="summary_large_image" dochead="1"><meta name="twitter:site" content="@edabit" dochead="1"><meta property="og:description" content="Edabit is like Duolingo for learning to code. Earn points for correct solutions, unlock achievements and level up. Our coding challenges make learning to code fun and easy." dochead="1"><meta property="og:image" content="https://s3.amazonaws.com/edabit-images/logo_wide_large.png" dochead="1"><meta property="og:site_name" content="edabit" dochead="1"><meta property="og:title" content="Explore 600+ FREE Coding Challenges | Edabit" dochead="1"><meta property="og:type" content="website" dochead="1"><meta name="description" content="We&#39;re like Duolingo for learning to code. Earn points for correct solutions, unlock achievements and level up. Our Python challenges make learning to code fun and easy." dochead="1"><link rel="icon" type="image/png" href="https://s3.amazonaws.com/edabit-images/logo_main_medium.png" dochead="1"><meta name="twitter:card" content="summary_large_image" dochead="1"><meta name="twitter:site" content="@edabit" dochead="1"><meta property="og:image" content="https://s3.amazonaws.com/edabit-images/logo_wide_large.png" dochead="1"><meta property="og:site_name" content="edabit" dochead="1"><meta property="og:type" content="website" dochead="1"><meta name="description" content="Create a function that takes two numbers as arguments and return their sum.

Examples
3, 2 ➞ 5

-3, -6 ➞ -9

7, 3 ➞ 10

Notes
Don&#39;t forget to return the result.
All tests contain valid numbers.
If you get stuck on a challenge, find help in the Resources tab.
If you&#39;re really stuck, unlock solutions in the Solutions tab." dochead="1"><meta name="keywords" content="javascript" dochead="1"><meta property="og:description" content="Create a function that takes two numbers as arguments and return their sum.

Examples
3, 2 ➞ 5

-3, -6 ➞ -9

7, 3 ➞ 10

Notes
Don&#39;t forget to return the result.
All tests contain valid numbers.
If you get stuck on a challenge, find help in the Resources tab.
If you&#39;re really stuck, unlock solutions in the Solutions tab." dochead="1"><meta property="og:title" content="Return the Sum of Two Numbers" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"><meta name="description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta name="keywords" content="python3" dochead="1"><meta property="og:description" content="Create a function that reverses a boolean value and returns the string " boolean="" expected"="" if="" another="" variable="" type="" is="" given.="" examples="" true="" ➞="" false="" 0="" "boolean="" none="" notes="" the="" input="" not="" a="" boolean,="" return="" string="" expected".="" you="" get="" stuck="" on="" challenge,="" find="" help="" in="" resources="" tab.="" you'r"="" dochead="1"><meta property="og:title" content="Flip the Boolean" dochead="1"></head>
<body>



  <script type="text/javascript">__meteor_runtime_config__ = JSON.parse(decodeURIComponent("%7B%22meteorRelease%22%3A%22METEOR%401.6.0.1%22%2C%22meteorEnv%22%3A%7B%22NODE_ENV%22%3A%22production%22%2C%22TEST_METADATA%22%3A%22%7B%7D%22%7D%2C%22PUBLIC_SETTINGS%22%3A%7B%22analyticsSettings%22%3A%7B%22Google%20Analytics%22%3A%7B%22trackingId%22%3A%22UA-91229704-1%22%7D%7D%2C%22hotjar%22%3A%7B%22hjid%22%3A%22399651%22%2C%22hjsv%22%3A%221%22%7D%7D%2C%22ROOT_URL%22%3A%22https%3A%2F%2Fedabit.com%22%2C%22ROOT_URL_PATH_PREFIX%22%3A%22%22%2C%22appId%22%3A%226oe24v3kjymx1952geg%22%2C%22autoupdateVersion%22%3A%22d9eb5fe74d65b0cb125c4b455c46ad3e304adcaf%22%2C%22autoupdateVersionRefreshable%22%3A%22359f95ec26ce24bf89d4026c8f75054fc1f482dc%22%2C%22autoupdateVersionCordova%22%3A%22none%22%7D"))</script>

  <script type="text/javascript" src="./Flip the Boolean_files/1c1a5f6a8e02c12bc28b183fc2585cf15580968d.js.download"></script>



<iframe name="_hjRemoteVarsFrame" title="_hjRemoteVarsFrame" id="_hjRemoteVarsFrame" style="display: none !important; width: 1px !important; height: 1px !important; opacity: 0 !important; pointer-events: none !important;" src="./Flip the Boolean_files/rcj-99d43ead6bdf30da8ed5ffcb4f17100c.html"></iframe><div id="react-root"><div data-reactroot="" id="MainLayout"><header><div id="Navbar"><div class="ui inverted text attached menu"><div class="ui container nav-wrapper"><a href="https://edabit.com/challenges" class="active link item" style="color: white; font-family: Avenir, Lato, Helvetica; font-size: 2.6rem; font-weight: 425; margin-left: -18px; margin-top: 4px;">edabit</a><a href="https://edabit.com/tinker" class="link item" style="letter-spacing: 0.037em;"><span>Tinker</span></a><a href="https://edabit.com/challenges" class="active link item" style="letter-spacing: 0.037em; border-bottom: 2px solid white; font-weight: 625; padding-bottom: 5px;"><span>Challenges</span></a><a href="https://edabit.com/practice" class="link item" style="letter-spacing: 0.037em;"><span>Practice</span></a><a href="https://edabit.com/help" class="link item" style="letter-spacing: 0.037em;"><span>Help</span></a><div class="right menu"><a class="item pointer"><div><!-- react-text: 425 -->140<!-- /react-text --><!-- react-text: 426 --> <!-- /react-text --><span>XP</span></div></a><div class="item"><div role="listbox" aria-expanded="false" class="ui floating top right pointing dropdown no-highlight" tabindex="0"><div class="text" role="alert" aria-live="polite"></div><i aria-hidden="true" class="alarm icon"></i><div class="menu transition" style="min-width: 160px; margin-right: -7px;"><div class="header" style="cursor: default;"><span>Notifications</span></div><div class="divider"></div><div role="option" aria-disabled="true" class="disabled item"><span>You don't have any notifications.</span></div><div class="divider"></div><div class="header"></div></div></div><div class="ui red mini circular floating label hidden">0</div></div><div class="item"><div><div role="listbox" aria-expanded="false" class="ui floating top right pointing dropdown" tabindex="0"><div class="text" role="alert" aria-live="polite"></div><i aria-hidden="true" class="plus icon"></i><div class="menu transition" style="margin-right: -7px;"><div role="option" class="item" style="min-width: 130px;"><span>New Challenge</span></div><a href="https://edabit.com/translate?firstLang=javascript" role="option" class="item"><span>New Translation</span></a><div role="option" class="item"><span>New Collection</span></div></div></div></div></div><div class="item"><div id="UserDropdown"><div role="listbox" aria-expanded="false" class="ui floating top right pointing dropdown" tabindex="0"><span><img src="./Flip the Boolean_files/avatar_generic.gif" class="ui mini avatar image"></span><div class="menu transition"><div role="option" aria-disabled="true" class="disabled item" style="width: 150px; margin-bottom: -5px;"><span>Signed in as</span><!-- react-text: 460 --> <!-- /react-text --><strong>pes04</strong></div><div class="divider"></div><a href="https://edabit.com/user/Yyid9Xqdj58tXhhBp" role="option" class="item"><span>Your Profile</span></a><a href="https://edabit.com/help" role="option" class="item"><span>Get Help</span></a><div role="option" class="item"><span>Settings</span></div><div class="divider"></div><div role="option" class="item"><span>Sign Out</span></div></div></div></div></div></div></div></div></div></header><main id="Main"><div id="Challenge" class="ui container" style="margin-top: 10px;"><div class="ui doubling stackable two column grid"><div class="ten wide column"><div class="ui left attached rail" style="margin-top: 58px;"><div class="ui basic right aligned segment" style="margin-right: -15px; float: right;"><div role="list" class="ui list"><div role="listitem" class="item"><div role="button" tabindex="0" class="SocialMediaShareButton SocialMediaShareButton--facebook"><i aria-hidden="true" class="facebook square large link icon"></i></div></div><div role="listitem" class="item"><div role="button" tabindex="0" class="SocialMediaShareButton SocialMediaShareButton--twitter"><i aria-hidden="true" class="twitter square large link icon"></i></div></div><div role="listitem" class="item"><div role="button" tabindex="0" class="SocialMediaShareButton SocialMediaShareButton--email"><i aria-hidden="true" class="mail square large link icon"></i></div></div></div></div></div><div class="rc-tabs rc-tabs-top"><div role="tablist" class="rc-tabs-bar no-highlight" tabindex="0"><div style="float: right;"><div role="listbox" aria-expanded="false" class="ui floating top right pointing dropdown" tabindex="0" style="margin-top: 10px;"><div class="text" role="alert" aria-live="polite"></div><i aria-hidden="true" class="ellipsis horizontal large link icon"></i><div class="menu transition" style="margin-right: -3px; min-width: 130px;"><div role="option" aria-disabled="false" class="item"><span>Add to bookmarks</span></div><div role="option" aria-disabled="false" class="item"><span>Add to collection</span></div><div class="divider"></div><div role="option" aria-disabled="false" class="item"><span>View analytics</span></div><div role="option" aria-disabled="false" class="item"><span>New translation</span></div><div role="option" aria-disabled="false" class="item"><span class="text">Reset code</span></div><div class="divider"></div><div role="option" aria-disabled="true" class="disabled item"><span>Edit</span></div></div></div></div><div class="rc-tabs-nav-container"><span unselectable="unselectable" class="rc-tabs-tab-prev rc-tabs-tab-btn-disabled"><span class="rc-tabs-tab-prev-icon"></span></span><span unselectable="unselectable" class="rc-tabs-tab-next rc-tabs-tab-btn-disabled"><span class="rc-tabs-tab-next-icon"></span></span><div class="rc-tabs-nav-wrap"><div class="rc-tabs-nav-scroll"><div class="rc-tabs-nav rc-tabs-nav-animated"><div class="rc-tabs-ink-bar rc-tabs-ink-bar-animated" style="display: block; transform: translate3d(108.797px, 0px, 0px); width: 53px;"></div><div role="tab" aria-disabled="false" aria-selected="false" class=" rc-tabs-tab"><span>Instructions</span></div><div role="tab" aria-disabled="false" aria-selected="true" class="rc-tabs-tab-active rc-tabs-tab"><span>Code</span></div><div role="tab" aria-disabled="false" aria-selected="false" class=" rc-tabs-tab"><span>Resources</span></div><div role="tab" aria-disabled="false" aria-selected="false" class=" rc-tabs-tab"><span>Solutions</span></div><div role="tab" aria-disabled="false" aria-selected="false" class=" rc-tabs-tab"><span>Comments</span></div></div></div></div></div></div><div class="rc-tabs-content rc-tabs-content-no-animated"><div role="tabpanel" aria-hidden="true" class="rc-tabs-tabpane rc-tabs-tabpane-inactive"><div><div class="grey-segment code-area instructions"><div class="ui header"><h2 class="content" style="margin-bottom: -5px; margin-top: -3px;">Flip the Boolean</h2><div class="sub header no-highlight" style="font-size: 13px; margin-top: 8px;"><span>Published by</span><!-- react-text: 3199 --> <!-- /react-text --><a href="https://edabit.com/user/BkPgkDQGHm66X4Qai">Matt</a><!-- react-text: 3201 --> <!-- /react-text --><span>in</span><!-- react-text: 3203 --> <!-- /react-text --><div role="listbox" aria-expanded="false" class="ui inline dropdown" tabindex="0" style="margin-right: -3px;"><div class="text" role="alert" aria-live="polite">Python</div><i aria-hidden="true" class="caret down icon"></i><div class="menu transition"><div class="header" style="cursor: default;"><span>Languages</span></div><div class="divider"></div><div role="option" aria-checked="false" class="item"><span class="text">JavaScript</span></div><div role="option" aria-checked="true" class="active item"><span class="text">Python</span></div><div role="option" aria-checked="false" class="item"><span class="text">Ruby</span></div><div class="divider"></div><div role="option" aria-disabled="false" class="item" style="min-width: 150px;"><i aria-hidden="true" class="plus icon"></i><span>Translate</span></div></div></div></div><div class="sub header no-highlight" style="margin-bottom: -3px; margin-left: -8px; margin-top: 8px;"><a class="ui tiny label" style="margin-right: -3px;"><!-- react-text: 3233 -->logic<!-- /react-text --></a></div></div><div><p><!-- react-text: 3240 -->Create a function that reverses a <!-- /react-text --><code>boolean</code><!-- react-text: 3242 --> value and returns the string <!-- /react-text --><code>"boolean expected"</code><!-- react-text: 3286 --> if another variable type is given.<!-- /react-text --></p><h3><!-- react-text: 3244 -->Examples<!-- /react-text --></h3><pre><code>True ➞ False

False ➞ True

0 ➞ "boolean expected"

None ➞ "boolean expected"</code></pre><h3><!-- react-text: 3288 -->Notes<!-- /react-text --></h3><ul><li><!-- react-text: 3291 -->If the input is not a boolean, return the string <!-- /react-text --><code>"boolean expected"</code><!-- react-text: 3293 -->.<!-- /react-text --></li><li><!-- react-text: 3295 -->If you get stuck on a challenge, find help in the <!-- /react-text --><strong><!-- react-text: 3297 -->Resources<!-- /react-text --></strong><!-- react-text: 3298 --> tab.<!-- /react-text --></li><li><!-- react-text: 3300 -->If you're <!-- /react-text --><em><!-- react-text: 3302 -->really<!-- /react-text --></em><!-- react-text: 3303 --> stuck, unlock solutions in the <!-- /react-text --><strong><!-- react-text: 3305 -->Solutions<!-- /react-text --></strong><!-- react-text: 3306 --> tab.<!-- /react-text --></li></ul></div></div><div style="float: left; margin-top: -5px; margin-bottom: 2px; font-size: 11px; cursor: default;"><i aria-hidden="true" class="yellow warning sign icon"></i><span>Are these instructions easy to understand?</span><!-- react-text: 3272 --> <!-- /react-text --><a style="cursor: pointer; margin-right: 2px; margin-left: 2px;"><span>Yes</span></a><!-- react-text: 3275 --> <!-- /react-text --><a style="cursor: pointer;"><span>No</span></a></div></div></div><div role="tabpanel" aria-hidden="false" class="rc-tabs-tabpane rc-tabs-tabpane-active"><div id="Code"><div class="ReactCodeMirror code-editor"><textarea autocomplete="off" style="display: none;">def reverse(arg):
	if isinstance(arg,bool):
		return not arg
	else:
		return "boolean expected"</textarea><div class="CodeMirror cm-s-default"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 87px; left: 68px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 30px; margin-bottom: -17px; border-right-width: 13px; min-height: 115px; min-width: 205px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 37px; top: 76px; height: 19px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">1</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">reverse</span>(<span class="cm-variable">arg</span>):</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">2</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">  </span><span class="cm-keyword">if</span> <span class="cm-builtin">isinstance</span>(<span class="cm-variable">arg</span>,<span class="cm-builtin">bool</span>):</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">3</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">  </span><span class="cm-tab" role="presentation" cm-text="	">  </span><span class="cm-keyword">return</span> <span class="cm-keyword">not</span> <span class="cm-variable">arg</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">4</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">  </span><span class="cm-keyword">else</span>:</span></pre></div><div class="CodeMirror-activeline" style="position: relative;"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: -30px; width: 30px;"></div><div class="CodeMirror-gutter-wrapper CodeMirror-activeline-gutter" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">5</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">  </span><span class="cm-tab" role="presentation" cm-text="	">  </span><span class="cm-keyword">return</span> <span class="cm-string">"boolean expected"</span></span></pre></div></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 115px;"></div><div class="CodeMirror-gutters" style="height: 128px; left: 0px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 29px;"></div></div></div></div></div><button class="ui red right floated button" role="button"><span>SUBMIT FINAL</span></button></div></div><div role="tabpanel" aria-hidden="true" class="rc-tabs-tabpane rc-tabs-tabpane-inactive"><div id="Resources"><div class="grey-segment"><div class="resources-padding-2"><a class="ui blue mini top right attached label" style="position: relative; z-index: 10; float: right; border-top-right-radius: 0px;"><i aria-hidden="true" class="plus icon"></i><!-- react-text: 3315 -->ADD RESOURCE<!-- /react-text --></a></div><div class="ui comments" style="margin-bottom: 6px; margin-top: 16px;"><div style="padding-bottom: 7.5px; padding-left: 15px; padding-top: 7.5px; width: 105%;"><div id="ResourceSingle"><div class="comment"><div class="content"><div class="author" style="font-size: 16px;"><a href="https://www.programiz.com/python-programming/methods/built-in/type" target="_blank" rel="nofollow"><!-- react-text: 3323 -->Python type() | Programiz<!-- /react-text --><i aria-hidden="true" class="external small icon" style="padding-left: 4px;"></i></a></div><span class="hostname">www.programiz.com</span><div class="text">If a single argument (object) is passed to type() built-in, it returns type of the given object. If three arguments (name, bases and dict) are passed, it returns a new type object.</div><div class="actions"><a class=""><span><!-- react-text: 3330 -->3<!-- /react-text --><!-- react-text: 3331 --> <!-- /react-text --></span><i aria-hidden="true" class="chevron up icon"></i></a><a class=""><i aria-hidden="true" class="chevron down icon"></i></a><a class=""><span class="hidden"><span>Edit</span></span></a></div></div></div></div></div><div style="padding-bottom: 7.5px; padding-left: 15px; padding-top: 7.5px; width: 105%;"><div id="ResourceSingle"><div class="comment"><div class="content"><div class="author" style="font-size: 16px;"><a href="https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance" target="_blank" rel="nofollow"><!-- react-text: 3344 -->What are the differences between type() and isinstance()?<!-- /react-text --><i aria-hidden="true" class="external small icon" style="padding-left: 4px;"></i></a></div><span class="hostname">stackoverflow.com</span><div class="text">Use isinstance() example</div><div class="actions"><a class=""><span><!-- react-text: 3351 -->1<!-- /react-text --><!-- react-text: 3352 --> <!-- /react-text --></span><i aria-hidden="true" class="chevron up icon"></i></a><a class=""><i aria-hidden="true" class="chevron down icon"></i></a><a class=""><span class="hidden"><span>Edit</span></span></a></div></div></div></div></div><div style="padding-bottom: 7.5px; padding-left: 15px; padding-top: 7.5px; width: 105%;"><div id="ResourceSingle"><div class="comment"><div class="content"><div class="author" style="font-size: 16px;"><a href="https://www.programiz.com/python-programming/methods/built-in/isinstance" target="_blank" rel="nofollow"><!-- react-text: 3365 -->Python isinstance() | Programiz<!-- /react-text --><i aria-hidden="true" class="external small icon" style="padding-left: 4px;"></i></a></div><span class="hostname">www.programiz.com</span><div class="text">The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).</div><div class="actions"><a class=""><span><!-- react-text: 3372 -->1<!-- /react-text --><!-- react-text: 3373 --> <!-- /react-text --></span><i aria-hidden="true" class="chevron up icon"></i></a><a class=""><i aria-hidden="true" class="chevron down icon"></i></a><a class=""><span class="hidden"><span>Edit</span></span></a></div></div></div></div></div></div></div></div></div><div role="tabpanel" aria-hidden="true" class="rc-tabs-tabpane rc-tabs-tabpane-inactive"></div><div role="tabpanel" aria-hidden="true" class="rc-tabs-tabpane rc-tabs-tabpane-inactive"></div></div></div></div><div class="six wide column"><div class="rc-tabs rc-tabs-top"><div role="tablist" class="rc-tabs-bar tabs-right no-highlight" tabindex="0" style="text-align: right;"><div class="rc-tabs-nav-container"><span unselectable="unselectable" class="rc-tabs-tab-prev rc-tabs-tab-btn-disabled"><span class="rc-tabs-tab-prev-icon"></span></span><span unselectable="unselectable" class="rc-tabs-tab-next rc-tabs-tab-btn-disabled"><span class="rc-tabs-tab-next-icon"></span></span><div class="rc-tabs-nav-wrap"><div class="rc-tabs-nav-scroll"><div class="rc-tabs-nav rc-tabs-nav-animated"><div class="rc-tabs-ink-bar rc-tabs-ink-bar-animated" style="display: block; transform: translate3d(81.5px, 0px, 0px); width: 70px;"></div><div role="tab" aria-disabled="false" aria-selected="false" class=" rc-tabs-tab"><span>Tests</span></div><div role="tab" aria-disabled="false" aria-selected="true" class="rc-tabs-tab-active rc-tabs-tab"><span>Console</span></div></div></div></div></div></div><div class="rc-tabs-content rc-tabs-content-no-animated"><div role="tabpanel" aria-hidden="true" class="rc-tabs-tabpane rc-tabs-tabpane-inactive"></div><div role="tabpanel" aria-hidden="false" class="rc-tabs-tabpane rc-tabs-tabpane-active"><div id="Console" class="console-segment custom-bullets"><ul><li class=""></li><!-- react-text: 3401 -->
<!-- /react-text --><li class="test-passed"><!-- react-text: 3403 -->Test&nbsp;Passed<!-- /react-text --></li><!-- react-text: 3404 -->
<!-- /react-text --><li class=""></li><!-- react-text: 3406 -->
<!-- /react-text --><li class="test-passed"><!-- react-text: 3408 -->Test&nbsp;Passed<!-- /react-text --></li><!-- react-text: 3409 -->
<!-- /react-text --><li class=""></li><!-- react-text: 3411 -->
<!-- /react-text --><li class="test-passed"><!-- react-text: 3413 -->Test&nbsp;Passed<!-- /react-text --></li><!-- react-text: 3414 -->
<!-- /react-text --><li class=""></li><!-- react-text: 3416 -->
<!-- /react-text --><li class="test-passed"><!-- react-text: 3418 -->Test&nbsp;Passed<!-- /react-text --></li><!-- react-text: 3419 -->
<!-- /react-text --><li class=""></li><!-- react-text: 3421 -->
<!-- /react-text --><li class="test-passed"><!-- react-text: 3423 -->Test&nbsp;Passed<!-- /react-text --></li><!-- react-text: 3424 -->
<!-- /react-text --><li class=""></li><!-- react-text: 3426 -->
<!-- /react-text --><li class="test-passed"><!-- react-text: 3428 -->Test&nbsp;Passed<!-- /react-text --></li><!-- react-text: 3429 -->
<!-- /react-text --><li class=""></li></ul></div></div></div></div><button class="ui black right floated button" role="button"><span>Skip</span></button></div></div></div></main><footer id="Footer"><div class="ui container no-highlight" style="margin: 0px; padding: 0px;"><div class="ui fitted horizontal divider" style="margin-bottom: 10px;"><i aria-hidden="true" class="code disabled icon"></i></div><div role="list" class="ui horizontal right floated list"><a href="https://edabit.com/contact" role="listitem" class="item"><span>Contact</span></a><a href="https://edabit.com/about" role="listitem" class="item"><span>About</span></a></div><div role="list" class="ui horizontal left floated list"><div role="listitem" class="disabled item">© 2018 Edabit</div><a href="https://edabit.com/docs/terms" role="listitem" class="item"><span>Terms</span></a><a href="https://edabit.com/docs/privacy" role="listitem" class="item"><span>Privacy</span></a><a href="https://edabit.com/roadmap" role="listitem" class="item"><span>Roadmap</span></a><a href="https://edabit.com/help" role="listitem" class="item"><span>Help</span></a></div></div></footer><div role="listbox" aria-expanded="false" class="ui basic button labeled upward dropdown icon" tabindex="0" style="bottom: 0px; margin-bottom: 4px; min-width: 122px; position: fixed; right: 0px;"><div class="text" role="alert" aria-live="polite">English</div><i aria-hidden="true" class="caret up icon"></i><div class="menu transition"><div role="option" aria-checked="true" aria-selected="true" class="active selected item" style="pointer-events: all;"><i class="gb flag"></i><span class="text">English</span></div><div role="option" aria-checked="false" aria-selected="false" class="item" style="pointer-events: all;"><i class="es flag"></i><span class="text">Español</span></div><div role="option" aria-checked="false" aria-selected="false" class="item" style="pointer-events: all;"><i class="fr flag"></i><span class="text">Français</span></div><div role="option" aria-checked="false" aria-selected="false" class="item" style="pointer-events: all;"><i class="de flag"></i><span class="text">Deutsch</span></div><div role="option" aria-checked="false" aria-selected="false" class="item" style="pointer-events: all;"><i class="br flag"></i><span class="text">Português</span></div><div role="option" aria-checked="false" aria-selected="false" class="item" style="pointer-events: all;"><i class="jp flag"></i><span class="text">日本語</span></div><div role="option" aria-checked="false" aria-selected="false" class="item" style="pointer-events: all;"><i class="cn flag"></i><span class="text">中文</span></div><div role="option" aria-checked="false" aria-selected="false" class="item" style="pointer-events: all;"><i class="ru flag"></i><span class="text">Pусский</span></div></div></div><div class="s-alert-wrapper"></div></div></div><div id="ads"></div></body></html>